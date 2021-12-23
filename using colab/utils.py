def top_N_influencers(unique_nodes,N):
  indexes=sorted(range(len(unique_nodes)), key = lambda sub: unique_nodes[sub])[-N:]
  return indexes