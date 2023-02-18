from collections import Counter

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def decompose_sum(s):
    return [(a,s-a) for a in range(2,int(s/2+1))]

# Generate all possible pairs
all_pairs = set((a,b) for a in range(2,100) for b in range(a+1,100) if a+b<100)
all_pairs = list(all_pairs)
print(len(all_pairs))

new_list = []
for i,j in all_pairs:
    if not (is_prime(i) and is_prime(j)):
        new_list.append([i,j])

print(len(new_list))
# Fact 1 --> Select pairs for which all sum decompositions have non-unique product
#product_counts = Counter(c*d for c,d in all_pairs)
#unique_products = set((a,b) for a,b in all_pairs if product_counts[a*b]==1)
#s_pairs = [(a,b) for a,b in all_pairs if
#    all((x,y) not in unique_products for (x,y) in decompose_sum(a+b))]

# Fact 2 --> Select pairs for which the product is unique
#product_counts = Counter(c*d for c,d in s_pairs)
#p_pairs = [(a,b) for a,b in s_pairs if product_counts[a*b]==1]

# Fact 3 --> Select pairs for which the sum is unique
#sum_counts = Counter(c+d for c,d in p_pairs)
#final_pairs = [(a,b) for a,b in p_pairs if sum_counts[a+b]==1]

#print(final_pairs)