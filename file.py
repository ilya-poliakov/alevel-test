print('ATM - insert amount of money:')

amount = int(input())

papers = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for paper in papers:
  papers_count = int(amount/paper)
  print(str(paper) +' - '+ str(papers_count))
  amount = amount - paper*papers_count
  if not (amount):
	break
	
