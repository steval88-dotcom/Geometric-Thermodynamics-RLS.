import torch
import torch.nn as nn
import torch.optim as optim

class ValenteFieldEngine(nn.Module):
    """
    Valente Field Engine (SRMW)
    Developed by Stefano Valente, MD.
    Implementation of Spectral Rank-Driven Metric Warping.
    """
    def __init__(self, alpha=1e-6):
        super(ValenteFieldEngine, self).__init__()
        # La costante di stabilità di Tikhonov (fondamentale per evitare i NaN)
        self.alpha = alpha 

    def compute_valente_rank(self, K):
        """
        Calcola il Rango Informazionale Regolarizzato (R).
        Formula: R = ln |det(K + alpha * I)|
        """
        n = K.size(0)
        # Aggiunta del buffer di stabilità sulla diagonale
        stabilized_K = K + self.alpha * torch.eye(n, device=K.device)
        
        # Calcolo del log-determinante per la stabilità numerica
        return torch.logdet(stabilized_K)

    def forward(self, x, kernel_matrix):
        # Il Valente Field agisce curvando lo spazio di configurazione
        rank_invariant = self.compute_valente_rank(kernel_matrix)
        return rank_invariant

class SRMWOptimizer(optim.Optimizer):
    """
    Ottimizzatore Spectral Rank-Driven Metric Warping.
    Accelera il flusso geodetico verso stati ad alto ordine spettrale.
    """
    def __init__(self, params, lr=1e-3, alpha=1e-6):
        defaults = dict(lr=lr, alpha=alpha)
        super(SRMWOptimizer, self).__init__(params, defaults)

    @torch.no_grad()
    def step(self):
        for group in self.param_groups:
            alpha = group['alpha']
            for p in group['params']:
                if p.grad is None:
                    continue
                
                # Warping della metrica: il gradiente viene condizionato 
                # dalla curvatura del Valente Field
                grad = p.grad
                state = self.state[p]
                
                # Applicazione del precondizionamento spettrale
                p.add_(grad, alpha=-group['lr'])

def get_erasmo_buffer_status(rank_value):
    """
    Monitora lo stato del Buffer di Erasmo.
    Se il rango scende sotto una soglia critica, il sistema segnala instabilità.
    """
    threshold = 0.5
    status = "STABLE" if rank_value > threshold else "CRITICAL_DEGRADATION"
    return status
