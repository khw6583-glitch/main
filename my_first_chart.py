import matplotlib.pyplot as plt

plt.rcParams["font.family"]="Malgun Gothic"

score=[88,73,97,67,99]

fig,ax=plt.subplots(figsize=(8,5))
ax.plot(score)

ax.set_title("내 점수 그래프")
fig.savefig("my_score_chart")