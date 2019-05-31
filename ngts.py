#Intento ingenuo del algoritmo NGTS
#po=posicion inicial del arbol
#T= arbol o grafo donde estan las posiciones
#po.hojas vector
#bmin = branches minimas
#lmin = hojas minimas
#pl = posicion del juego
#ml = jugadas escogidas(candidate moves)
def NGTS(po,T):
    po = T.root
    mybest=0
    if(T.root is None):
        return po
    if(po.hojas>T.Lmin):
        for( i in range len(po.hojas)):
            evaluatedvaluelistGPU=leafcalculationfunctionGPU(po) #GPU
            for i in range len(evaluatedvaluelistGPU) :
                evaluatedvaluelistGPU[i].padre = evaluatedvaluelistGPU[i]
                if(evaluatedvaluelistGPU[i]==T.root):
                    mybest=evaluatedvaluelistGPU[i]
                #no entiendo bien esta parte
                Prune(T)
    if(po.hojas>0):
        leaf = T.oneleaf()
        evaluatedvalueCPU=leafcalculationfunctionCPU(leaf) #CPU
        if(evaluatedvaluelistGPU==T.root):
                    mybest=evaluatedvaluelistCPU
        Prunte(T)
    if(po.branches>T.bmin):
        for(i in range len(po.branches)):
            childnodelistGPU=branchcalculationfunctionGPU(po)
            for i in range len(childnodelistGPU):
                update(T,childnodelistGPU)
    if(po.branches>0):
        leaf = T.oneleaf()
        childnodeCPU=branchcalculationfunctionCPU(po)
        update(T,childnodeCPU)
def branchcalculationfunctionGPU(pl,legalpoints):
    rank =get_rank()
    for p in legalpoints:
        # reconocer p respecto a las reglas del juego 
        # calcular puntaje
        # acumular puntaje
    #guardar jugadas disponibles en ml
    return ml
def leafcalculationfunctionGPU(pl,nonemptymoves):
    rank = get_rank()
    for p in nonemptymoves:
        # reconocer p respecto a las reglas del juego 
        # calcular puntaje
        # acumular puntaje
    #guardar todos los valore evaluados en V
    return V
    