def fifo(paginas, quadros):
    memoria = []
    ordem = []
    for p in paginas:
        if p not in memoria:
            if len(memoria) < quadros:
                memoria.append(p)
                ordem.append(p)
            else:
                removido = ordem.pop(0)
                idx = memoria.index(removido)
                memoria[idx] = p
                ordem.append(p)
        else:
            pass
    return memoria

def lru(paginas, quadros):
    memoria = []
    usado = []
    for p in paginas:
        if p in memoria:
            usado.remove(p)
            usado.append(p)
        else:
            if len(memoria) < quadros:
                memoria.append(p)
                usado.append(p)
            else:
                lru_pagina = usado.pop(0)
                idx = memoria.index(lru_pagina)
                memoria[idx] = p
                usado.append(p)
    return memoria

def mru(paginas, quadros):
    memoria = []
    usado = []
    for p in paginas:
        if p in memoria:
            usado.remove(p)
            usado.append(p)
        else:
            if len(memoria) < quadros:
                memoria.append(p)
                usado.append(p)
            else:
                mru_pagina = usado.pop()
                i = memoria.index(mru_pagina)
                memoria[i] = p
                usado.append(p)
    return memoria

def testar_algoritmos():
    quadros = 8
    sequencias = [
        ([4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7], 7),
        ([4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11], 11),
        ([4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11], 11)
    ]
    
    for seq, pagina in sequencias:
        print(f"Sequência: {seq}")
        
        mem_fifo = fifo(seq, quadros)
        mem_lru = lru(seq, quadros)
        mem_mru = mru(seq, quadros)
        
        print(f"FIFO: Memória final = {mem_fifo}")
        print(f"Página {pagina} está no quadro {mem_fifo.index(pagina)+1 if pagina in mem_fifo else 'NÃO ESTÁ'}")
        
        print(f"LRU:  Memória final = {mem_lru}")
        print(f"Página {pagina} está no quadro {mem_lru.index(pagina)+1 if pagina in mem_lru else 'NÃO ESTÁ'}")
        
        print(f"MRU:  Memória final = {mem_mru}")
        print(f"Página {pagina} está no quadro {mem_mru.index(pagina)+1 if pagina in mem_mru else 'NÃO ESTÁ'}")

testar_algoritmos()
