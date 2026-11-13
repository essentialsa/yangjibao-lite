import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.ticker import MultipleLocator

# ---------- Style ----------
FONT = "Noto Sans CJK SC"
if FONT not in [f.name for f in fm.fontManager.ttflist]:
    for cand in ["WenQuanYi Micro Hei", "Noto Sans CJK JP", "SimHei"]:
        if cand in [f.name for f in fm.fontManager.ttflist]:
            FONT = cand
            break

plt.rcParams.update({
    "font.family": FONT,
    "axes.unicode_minus": False,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#D1D5DB",
    "axes.linewidth": 0.8,
    "text.color": "#1F2937",
    "axes.labelcolor": "#374151",
    "xtick.color": "#4B5563",
    "ytick.color": "#4B5563",
    "font.size": 12,
})

INK = "#1F2937"
MUTED = "#6B7280"
GRID = "#E5E7EB"
NAVY = "#1B3A5C"
TEAL = "#2A7F7F"
AMBER = "#C88A2E"
RED = "#B54A3F"
GRAY = "#9CA3AF"

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
os.makedirs(OUT, exist_ok=True)


def clean(ax, grid_axis="x"):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#D1D5DB")
    ax.spines["bottom"].set_color("#D1D5DB")
    ax.grid(axis=grid_axis, color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved", path)


# ---------- Chart 1: household penetration gap ----------
fig, ax = plt.subplots(figsize=(9.2, 3.8))
labels = ["中国家庭", "日本 / 欧美家庭"]
vals = [5, 70]
colors = [RED, TEAL]
bars = ax.barh(labels, vals, color=colors, height=0.22, zorder=3)
bars[0].set_alpha(0.92)
ax.set_xlim(0, 82)
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.set_xlabel("家庭安全应急产品配备率（%）")
clean(ax, "x")
ax.text(5.6, 0, "不足 5%", va="center", ha="left", fontsize=17, fontweight="bold", color=RED)
ax.text(70.6, 1, "超过 70%", va="center", ha="left", fontsize=17, fontweight="bold", color=TEAL)
ax.set_title("4.9 亿户家庭，配备率不足 5%", loc="left", fontsize=20, fontweight="bold", pad=24)
ax.text(0, 1.02, "示意：中国不足 5%，日本 / 欧美超过 70%", transform=ax.transAxes,
        fontsize=12, color=MUTED)
fig.text(0.01, -0.06, "数据来源：中国信通院《以〈规范条件〉推动家庭安全应急产品行业健康发展》；央广网（2026-08）",
         fontsize=9, color=MUTED)
save(fig, "chart_1_penetration.png")


# ---------- Chart 2: national spot-check failure rate ----------
fig, ax = plt.subplots(figsize=(9.6, 4.8))
items = ["防火门", "过滤式消防自救呼吸器", "手提式干粉灭火器"]
vals = [9.4, 9.1, 4.2]
colors = [GRAY, RED, AMBER]
y = list(range(len(items)))[::-1]
bars = ax.barh(y, vals, color=colors, height=0.5, zorder=3)
ax.set_yticks(y)
ax.set_yticklabels(items, fontsize=13)
ax.set_xlim(0, 12)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.set_xlabel("监督抽查不合格率（%）")
clean(ax, "x")
for yi, v in zip(y, vals):
    ax.text(v + 0.22, yi, f"{v:.1f}%", va="center", fontsize=14, fontweight="bold", color=INK)
ax.set_title("每 100 件消防产品，仍有 4–9 件不合格", loc="left", fontsize=20, fontweight="bold", pad=18)
ax.text(0, 1.02, "2024 年国家市场监管总局监督抽查结果", transform=ax.transAxes, fontsize=12, color=MUTED)
fig.text(0.01, -0.08, "数据来源：市场监管总局抽查结果，新华社《“救命器材”竟成“摆设”》（2025-11-11）",
         fontsize=9, color=MUTED)
save(fig, "chart_2_failure_rate.png")


# ---------- Chart 3: e-commerce price ladder ----------
fig, axes = plt.subplots(1, 2, figsize=(13.6, 6.2), gridspec_kw={"width_ratios": [1.05, 1.0]})

# Left: extinguishers
ax = axes[0]
names = ["京玺 MSWJ600（600ml 水基）", "得力 MSWJ620C（620ml 水基）", "准航 21B（620ml 水基）",
         "火焰战士 MFJ520L（520g 干粉）", "援邦 MF/ABCE4（4kg 干粉）", "神龙 3L 水基（价格锚点）"]
vals = [13.9, 13.9, 20.8, 28.8, 64.9, 132.0]
y = list(range(len(names)))[::-1]
cols = [TEAL, TEAL, TEAL, AMBER, AMBER, TEAL]
ax.barh(y, vals, color=cols, height=0.56, zorder=3)
ax.set_yticks(y)
ax.set_yticklabels(names, fontsize=10.5)
ax.set_xlim(0, 155)
ax.set_xlabel("参考价（元 / 具）")
clean(ax, "x")
for yi, v in zip(y, vals):
    ax.text(v + 2.5, yi, f"¥{v:g}", va="center", fontsize=11.5, fontweight="bold", color=INK)
ax.set_title("灭火器：¥14 – ¥132", loc="left", fontsize=16, fontweight="bold", pad=14)

# Right: masks
ax = axes[1]
names2 = ["趣行 TZL30", "准航 TZL30", "浙星 TZL-30", "凯安宝 TZL30E", "兴安 TZL30",
          "海康威视 TZL30", "浙安 TZL30A（反光款）", "中加沃安 TZL30 披肩款"]
vals2 = [17.29, 18.49, 23.0, 24.8, 31.1, 37.9, 53.4, 87.0]
y2 = list(range(len(names2)))[::-1]
cols2 = [NAVY] * 6 + [RED, RED]
ax.barh(y2, vals2, color=cols2, height=0.58, zorder=3)
ax.set_yticks(y2)
ax.set_yticklabels(names2, fontsize=10.5)
ax.set_xlim(0, 102)
ax.set_xlabel("参考价（元 / 只）")
clean(ax, "x")
for yi, v in zip(y2, vals2):
    ax.text(v + 1.5, yi, f"¥{v:g}", va="center", fontsize=11.5, fontweight="bold", color=INK)
ax.set_title("消防面具：¥17 – ¥87", loc="left", fontsize=16, fontweight="bold", pad=14)

fig.suptitle("同规格价差可达 6 倍：价格不是合规的代理变量", x=0.01, y=1.06,
             ha="left", fontsize=20, fontweight="bold", color=INK)
fig.text(0.01, -0.03, "数据来源：京东消费决策中心公开选购指南（2026-10）；什么值得买神龙 3L 历史价格。"
         "左图绿色为水基、橙色为干粉；右图同为 TZL30 额定 30 分钟。价格为参考区间，非实时报价",
         fontsize=9, color=MUTED)
fig.tight_layout(w_pad=3.2)
save(fig, "chart_3_price_ladder.png")


# ---------- Chart 4: three configuration budgets ----------
fig, ax = plt.subplots(figsize=(9.8, 5.4))
plans = ["入门档\n出租屋 / 车载", "标准档\n两居 / 三口之家", "强化档\n高层 / 有老人"]
ext = [27.8, 196.9, 196.9]
mask = [55.5, 73.96, 213.6]
x = range(len(plans))
b1 = ax.bar(x, ext, width=0.5, color=AMBER, label="灭火器", zorder=3)
b2 = ax.bar(x, mask, width=0.5, bottom=ext, color=TEAL, label="消防面具", zorder=3)
ax.set_xticks(list(x))
ax.set_xticklabels(plans, fontsize=12.5)
ax.set_ylim(0, 480)
ax.set_ylabel("配置成本（元）")
clean(ax, "y")
for i, (a, b) in enumerate(zip(ext, mask)):
    total = a + b
    ax.text(i, total + 12, f"¥{int(total + 0.5)}", ha="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(i, a / 2, f"¥{a:.0f}", ha="center", va="center", fontsize=11, color="white", fontweight="bold")
    ax.text(i, a + b / 2, f"¥{b:.0f}", ha="center", va="center", fontsize=11, color="white", fontweight="bold")
ax.legend(frameon=False, loc="upper left", fontsize=11.5)
ax.set_title("三档家庭消防配置：¥83 到 ¥411", loc="left", fontsize=20, fontweight="bold", pad=18)
ax.text(0, 1.02, "按电商参考价测算，不含灭火毯、独立烟感与安装费用", transform=ax.transAxes,
        fontsize=12, color=MUTED)
fig.text(0.01, -0.08, "测算口径：入门档 = 2×620ml 水基 + 3×TZL30；标准档 = 3L 水基 + 4kg 干粉 + 4×TZL30；"
         "强化档 = 3L 水基 + 4kg 干粉 + 4×TZL30A 反光款。4kg 为保守上限，家用 3kg 干粉成本更低",
         fontsize=9, color=MUTED)
save(fig, "chart_4_budget.png")

print("all done")
