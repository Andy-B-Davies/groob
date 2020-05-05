import copy
import itertools
# def minimise_basis(G):
#     i=0
#     while i < len(G):
#         for j in G:
#             if G[-1-i].lead_term() | j.lead_term() and not (j == G[-1-i]):
#                 G.remove(G[-1-i])
#                 break
#         i+=1
#     print(G)




def minimise_basis(G):
    # TODO clean up

    H = G.copy()
    M = []
    while H:
        p = H.pop()
        
        print(f"try p={p}")
        print(list(itertools.chain(H, M)))

        for q in itertools.chain(H, M):
            if p.lead_term() | q.lead_term():
                print(f"p_lead = {p.lead_term()}")
                print(f"q_lead = {q.lead_term()}")
                print(f"q_lead divides into p_lead = {p.lead_term() | q.lead_term()}")
                
                print(f"remove p = {p}")
                break
        else:
            print(f"add back {p}")
            M.append(p)


        # if any( p.lead_term() | q.lead_term() for q in itertools.chain(H, M)):
        #     print(f"p_lead = {p.lead_term()}")
        #     print(f"q_lead = {q.lead_term()}")
        #     print(f"q_lead divides into p_lead = {p.lead_term() | q.lead_term()}")
            
        #     print(f"remove p = {p}")
        # else:
        #     print(f"add back {p}")
        #     M.append(p)

    return M
            
        
