# Lebesgue 积分

Lebesgue 积分定义在测度空间上：

$$(\Omega, \mathcal{F},\mu)$$

其中：

- $\Omega$：样本空间，即底层集合

- $\mathcal{F}$：可测集合族

- $\mu$：测度，用来表示集合的“大小”

在概率论中，常写成：

$$(\Omega, \mathcal{F},\mathbb{P})$$

其中 $\mathbb{P}$ 是概率测度。

随机变量 $X$ 的期望，本质上就是 Lebesgue 积分：

$$\mathbb{E}[X] = \int_{\Omega} X(\omega) d\mathbb{P}(\omega)$$

最基本的函数是指示函数：

$$\mathbf{1} _A(\omega) = \left\{\begin{matrix}
 1,\omega\in A\\
0,\omega \notin A
\end{matrix}\right.$$

它的积分定义为：

$$\int_{\Omega}\mathbf{1}_A d\mu = \mu(A)$$


在集合 $A$ 上取值为 1，在其他地方取值为 0，因此它的积分就是集合 $A$ 的测度。

在概率论中：

$$\int_{\Omega} \mathbf{1}_A d\mathbb{P} = \mathbb{P} (A)$$

因此：

$$\mathbb{E}[\mathbf{1}_A] = \mathbb{P}(A)$$

设

$$(\Omega, \mathcal{F}, \mu)$$

是一个测度空间。若函数

$$\varphi: \Omega \to [0,\infty]$$

满足以下两个条件，就称它是非负简单函数：

1. $\varphi$ 是可测函数；

2. $\varphi$ 只取有限多个非负值。

也就是说，存在有限多个非负实数：

$$y_1,y_2,\dots,y_m \ge 0$$

使得

$$\varphi(\Omega) \subseteq \{y_1,y_2,\dots,y_m\}$$

并且，对每个取值 $y_j$，集合

$$E_j = \{\omega \in \Omega: \varphi(\omega) = y_j\}$$

都是可测集合，也就是 $E_j \in \mathcal{F}$。

于是可以写成标准表示：

$$\boxed{\varphi = \sum_{j = 1} ^m y_j \mathbf{1} _{E_j}}$$

其中 $E_1,E_2,\dots,E_m$ 两两不交。

设 $$f:\Omega\to [0,+\infty]$$

它未必只取有限多个值，因此不一定是简单函数。

Lebesgue 积分的定义是：

$$\int_{\Omega} f d\mu = \sup \left\{ \int_{\Omega} \varphi d\mu: 0 \le \varphi(\omega)\le f(\omega),\ \forall \omega \in \Omega,\ \varphi \in \mathcal{S}^+ \right\}$$

其中 $\mathcal{S}^+$ 表示非负简单函数全体。

也就是说，用所有不超过 $f$ 的非负简单函数从下方逼近 $f$，再取这些简单函数积分的上确界。

Lebesgue 积分并不是直接对 $f$ 本身积分，而是先对阶梯函数积分，再让阶梯函数逐步逼近 $f$。

下面来看 Lebesgue 积分的一个典型优势。

定义：

$$f(x) = \mathbf{1}_{\mathbb{Q} \cap [0,1]}(x)$$

也就是：当 $x \in \mathbb{Q} \cap [0,1]$ 时 $f(x)=1$，否则 $f(x)=0$。等价地，

$$f(x) = \begin{cases}
1, & x \in \mathbb{Q} \cap [0,1] \\
0, & x \in [0,1] \setminus \mathbb{Q}
\end{cases}$$

这个函数在 $[0,1]$ 上处处不连续，因此 Riemann 不可积。

但 Lebesgue 积分却很容易计算。

因为有理数集合 $\mathbb{Q} \cap [0,1]$ 是可数集，而可数集的 Lebesgue 测度为 0。

所以：

$$\int_0^1 \mathbf{1}_{\mathbb{Q} \cap [0,1]} dx = \mu(\mathbb{Q} \cap [0,1]) = 0$$

因此：

$$\int_0^1 f dx = 0$$
# 无穷级数的定义

对于一个非负数列

$$a_1,a_2,\cdots ,...$$

它的无穷级数定义为部分和的极限:

$$\boxed{\sum_{k= 1} ^\infty a_k = \lim_{n\to \infty} \sum_{k = 1} ^n a_k}$$


# 测度的下连续性

测度的下连续性，也叫从下方连续。

它说的是：若有一列可测集合

$$A_1 \subset A_2 \subset A_3 \subset \dots$$

也就是集合越来越大，那么

$$\boxed{\mu(\cup _{n=1}^\infty A_n) = \lim_{n \to \infty} \mu(A_n)}$$

设 $A_1\subseteq A_2\subseteq A_3\subseteq \dots$。

令：

$$B_1 = A_1$$

$$B_2 = A_2 - A_1$$

$$B_3 = A_3 - A_2$$

一般地：

$$B_n = A_n - A_{n - 1}$$

这些 $B_n$ 两两不交。

而且：

$$A_n = B_1 \cup B_2 \cup \dots \cup B_n$$

所以由测度的有限可加性：

$$\mu(A_n) = \sum_{k = 1}^n \mu(B_k)$$

另一方面：

$$\cup_{n = 1} ^\infty A_n = \cup_{k = 1} ^\infty B_k$$

由于 $B_k$ 两两不交，由测度的可列可加性，有：

$$\mu(\cup_{n=1}^\infty A_n) = \mu(\cup_{k=1}^\infty B_k) = \sum_{k=1}^\infty \mu(B_k)$$

而：

$$\lim_{n\to \infty}\mu(A_n) = \lim_{n\to \infty}\sum_{k = 1} ^n \mu(B_k) = \sum_{k = 1}^\infty \mu(B_k)$$

所以：

$$\mu(\cup_{n = 1} ^\infty A_n) = \lim_{n\to \infty} \mu(A_n)$$

证毕。

# 单调收敛定理

设

$$(\Omega,\mathcal{F},\mu)$$

是一个测度空间。设 $f_1,f_2,f_3,\dots$ 是一列非负可测函数，并且满足

$$0\le f_1 \le f_2\le f_3 \le \dots$$

这里的不等式是逐点成立的，也就是对每个 $\omega \in \Omega$ 都有

$$0\le f_1(\omega) \le f_2(\omega) \le f_3(\omega) \le \dots$$

假设它们逐点收敛到函数 $f$：

$$f_n(\omega) \uparrow f(\omega)$$

那么单调收敛定理说：

$$\boxed{\int_{\Omega} fd\mu = \lim_{n\to \infty} \int_{\Omega} f_n d\mu}$$

也可写成：

$$\boxed{\int_{\Omega} \lim_{n\to \infty} f_n d\mu = \lim_{n\to\infty} \int_{\Omega} f_n d\mu}$$

在概率论里，如果把测度 $\mu$ 换成概率测度 $\mathbb{P}$，积分就是期望：

$$\mathbb{E}[f] = \int_{\Omega} fd \mathbb{P}$$

所以概率版本是：

$$0 \le X_1 \le X_2 \le \dots,\quad X_n \uparrow X \Rightarrow \mathbb{E}[X_n] \uparrow \mathbb{E}[X]$$

这里允许积分或期望取值为 $\infty$。

## 先证明 $\lim \int f_n \le \int f$

因为 $f_n \le f$，

所以由积分的单调性，

$$\int_{\Omega} f_n d\mu \le \int_{\Omega} f d\mu$$

因此：

$$\lim_{n \to \infty}\int_{\Omega} f_n d\mu \le \int_{\Omega} f d\mu$$

这一方向很容易。

真正困难的是反过来证明：

$$\int_{\Omega} f d\mu \le \lim_{n\to \infty} \int_{\Omega} f_n d\mu$$

## 证明反方向

令

$$L = \lim_{n\to \infty}\int_{\Omega} f_n d\mu$$

因为 $\int f_n$ 单调递增，所以这个极限存在，可能是有限数，也可能是 $+\infty$。

我们要证明：

$$\int_{\Omega} f d\mu \le L$$

根据 Lebesgue 积分的定义，只要证明：对任意满足 $0 \le \varphi \le f$ 的非负简单函数 $\varphi$，都有

$$\int_{\Omega} \varphi d\mu \le L$$

因为 $\int f$ 正是这些 $\varphi$ 的上确界。

## 固定一个简单函数 $\varphi \le f$

取任意非负简单函数 $\varphi$，满足 $0\le \varphi \le f$。

再取一个常数：

$$0 < a < 1$$

定义集合：

$$E_n = \{\omega \in \Omega : f_n(\omega) \ge a\varphi(\omega) \}$$

因为

$$f_n(\omega) \uparrow f(\omega)$$

且

$$\varphi(\omega) \le f(\omega)$$

所以对每个 $\omega$，最终都会有

$$f_n(\omega) \ge a\varphi(\omega)$$

这里必须选取 $a < 1$，而不能取 $a = 1$。

因为可能出现：

$$f_n(\omega) \uparrow f(\omega) = \varphi(\omega)$$

但每个 $f_n(\omega)$ 都严格小于 $\varphi(\omega)$。此时只要取 $a < 1$，就能保证最终超过 $a\varphi(\omega)$。

因此 $E_n \uparrow \Omega$。

更严格地说，在 $\varphi > 0$ 的地方会被最终覆盖，而在 $\varphi = 0$ 的地方则自动满足。

## 构造逐点不等式

在 $E_n$ 上，有 $f_n \ge a\varphi$；

在 $E_n$ 外，右端取 0。

所以逐点成立：

$$f_n \ge a\varphi \mathbf{1}_{E_n}$$

对两边积分：

$$\int_{\Omega} f_n d\mu \ge a\int_{\Omega} \varphi \mathbb{1} _{E_n} d\mu$$

因此：

$$L \ge a\int_{\Omega} \varphi \mathbb{1}_{E_n} d\mu$$

对所有 $n$ 都成立。

设 $n \to \infty$。

因为 $E_n \uparrow \Omega$，

所以 $\varphi \mathbf{1}_{E_n} \uparrow \varphi$。

由于 $\varphi$ 是简单函数，这一步可以直接算出来：

如果 $\varphi = \sum_{j=1}^m c_j \mathbf{1}_{A_j}$

其中 $A_j$ 两两不交，则：

$$\varphi \mathbb{1}_{E_n} = \sum_{j = 1} ^ m c_j \mathbb{1} _{A_j \cap E_n}$$

于是：

$$\int_{\Omega} \varphi \mathbf{1}_{E_n} d\mu = \sum_{j=1}^m c_j \mu(A_j \cap E_n)$$

因为：

$$E_n\uparrow \Omega$$

所以：

$$A_j \cap E_n \uparrow A_j$$

根据测度的下连续性：

$$\mu(A_j \cap E_n) \uparrow \mu(A_j)$$

因此：

$$\int_{\Omega} \varphi \mathbb{1} _{E_n} d\mu \uparrow \int_{\Omega} \varphi d\mu$$

于是令 $n\to \infty$，得到：

$$L \ge a\int_{\Omega} \varphi d\mu$$

上式对任意

$$0 < a < 1$$

都成立，所以再令

$$a \uparrow 1$$

得到：

$$L \ge \int_{\Omega}\varphi d\mu$$

由于 $\varphi$ 是任意满足

$$0\le \varphi \le f$$

的非负简单函数，所以对所有这样的 $\varphi$，都有

$$\int_{\Omega} \varphi d\mu \le L$$

取上确界：

$$\int_{\Omega} fd\mu = \sup_{\substack{0\le \varphi \le f \\ \varphi \in \mathcal{S}^+}} \int_{\Omega} \varphi d\mu \le L$$

也就是：

$$\int_{\Omega} fd\mu \le \lim_{n\to \infty}\int_{\Omega} f_n d\mu$$

结合另一方向的不等式，得到：

$$\boxed{\int_{\Omega} fd\mu = \lim_{n\to \infty} \int_{\Omega} f_n d\mu}$$

单调收敛定理证毕。

## 为什么证明要用 $a < 1$

这是证明里最巧妙的一步。

假设：

$$f_n(\omega) = 1 - \frac{1}{n}$$

而

$$f(\omega) = 1$$

那么：

$$f_n(\omega) \uparrow f(\omega)$$

如果取 $\varphi(\omega) = 1$，虽然

$$\varphi(\omega) = f(\omega)$$

但对所有 $n$，都有

$$f_n(\omega) < \varphi(\omega)$$

所以不能保证最终出现

$$f_n \ge \varphi$$

但如果取：

$$a = 0.99$$

那么最终一定有：

$$f_n \ge 0.99\varphi$$

所以证明里先把目标压低一点，用

$$a\varphi$$

代替 $\varphi$，最后再令

$$a \uparrow 1$$

这是一个非常经典的技巧。

# Tonelli 定理

Tonelli 定理说的是：对非负函数，积分的顺序可以交换。

在概率论里，它最重要的形式是：设

$$Z_1,Z_2,Z_3,\dots$$

是一列非负随机变量：

$$Z_n(\omega) \ge 0$$

那么：

$$\boxed{\mathbb{E}\left[\sum_{n=1}^{\infty} Z_n\right] = \sum_{n=1}^{\infty} \mathbb{E}[Z_n]}$$

注意：关键条件是非负性。只要每一项非负，即使两边都是 $+\infty$，等式也仍然成立。

## 证明

令

$$S_N(\omega) = \sum_{n = 1}^N Z_n(\omega)$$

因为每个 $Z_n \ge 0$，所以

$$S_1(\omega) \le S_2(\omega) \le S_3(\omega)\le \dots$$

并且

$$S_N(\omega) \uparrow S(\omega)$$

其中

$$S(\omega) = \sum_{n=1}^{\infty} Z_n(\omega)$$

根据单调收敛定理：

$$\mathbb{E}[S] = \lim_{N\to \infty} \mathbb{E}[S_N]$$

也就是：

$$\mathbb{E}\left[\sum_{n=1}^{\infty} Z_n\right] = \lim_{N\to \infty} \mathbb{E}\left[\sum_{n=1}^{N} Z_n\right]$$

有限和可以交换期望：

$$\mathbb{E}\left[\sum_{n=1}^{N} Z_n\right] = \sum_{n=1}^{N} \mathbb{E}[Z_n]$$

所以：

$$\mathbb{E}\left[\sum_{n=1}^{\infty} Z_n\right] = \lim_{N\to \infty} \sum_{n=1}^{N} \mathbb{E}[Z_n]$$

而右边正是无穷级数：

$$\sum_{n=1}^{\infty} \mathbb{E}[Z_n]$$

因此：

$$\boxed{\mathbb{E}\left[\sum_{n=1}^{\infty} Z_n\right] = \sum_{n=1}^{\infty} \mathbb{E}[Z_n]}$$

# 乘积测度

设有两个测度空间：

$$(X, \mathcal{A}, \mu)$$

$$(Y, \mathcal{B}, \nu)$$

其中：

- $X,Y$ 是两个底层空间；

- $\mathcal{A},\mathcal{B}$ 是可测集合族；

- $\mu, \nu$ 是测度。

现在我们想在乘积空间

$$X\times Y$$

上定义一个新的测度。

一个点可以写成 $(x,y)$：第一坐标来自 $X$，第二坐标来自 $Y$。

要谈测度，首先要知道哪些集合是可测的。

在 $X \times Y$ 上，我们先看最基本的集合 $A\times B$，

其中 $A \in \mathcal{A}, B \in \mathcal{B}$。

这种集合叫做可测矩形。

但乘积空间里还有更复杂的集合，例如多个矩形的并、交、补、可数并等。

因此我们定义乘积 $\sigma$ 代数：

$$\boxed{\mathcal{A} \otimes \mathcal{B} = \sigma( \{ A\times B: A\in \mathcal{A} ,B\in \mathcal{B}\})}$$

$\mathcal{A} \otimes \mathcal{B}$ 是由所有可测矩形生成的最小 $\sigma$ 代数，也就是我们在乘积空间上允许测量的集合族。

乘积测度记作

$$\mu \otimes \nu$$

它是定义在

$$(X \times Y, \mathcal{A} \otimes \mathcal{B})$$

上的测度，并且满足最核心的性质：

$$(\mu \otimes \nu) (A\times B) = \mu(A) \nu(B)$$

其中

$$A \in \mathcal{A}, B\in \mathcal{B}$$

这就是乘积测度的核心：矩形的测度等于两条边测度的乘积。

如果 $\mu,\nu$ 是概率测度，那么

$$(\mu \otimes \nu)(A\times B) = \mu(A) \nu(B)$$

就表示两件事同时发生的概率等于各自概率的乘积。

## 乘积测度与独立性

设

$$E = A \times Y$$

表示只关心第一坐标的事件。

设

$$F = X\times B$$

表示只关心第二坐标的事件。

那么

$$E\cap F =(A\times Y )\cap (X\times B) = A \times B$$

所以

$$(\mu \otimes \nu)(E \cap F) = (\mu \otimes \nu)(A \times B)$$

由乘积测度的定义：

$$(\mu \otimes \nu)(E \cap F) = \mu(A)\nu(B)$$

另一方面：

$$(\mu \otimes \nu)(E) = (\mu \otimes \nu)(A\times Y) = \mu(A) \nu(Y)$$

如果 $\nu$ 是概率测度，则 $\nu(Y)=1$，所以 $(\mu \otimes \nu)(E) = \mu(A)$。

同理，$(\mu \otimes \nu)(F) = \nu(B)$。

因此

$$(\mu \otimes \nu)(E \cap F) = (\mu \otimes \nu)(E) \cdot (\mu \otimes \nu)(F)$$

这正是独立性的含义。

所以：

**乘积概率测度保证第一坐标事件和第二坐标事件相互独立。**
# 独立性

设二维随机游走为

$$S_n = (X_n, Y_n)$$

其中

$$X_n = \epsilon_1 + \epsilon_2 + \cdots + \epsilon_n$$

$$Y_n = \eta_1 + \eta_2 + \cdots + \eta_n$$

每个横向增量满足

$$\mathbb{P}(\epsilon_k = 1) = \mathbb{P}(\epsilon_k = -1) = \frac{1}{2}$$

每个纵向增量满足

$$\mathbb{P}(\eta_k = 1) = \mathbb{P}(\eta_k = -1) = \frac{1}{2}$$

并且

$$\epsilon_1,\epsilon_2,\dots$$

与

$$\eta_1,\eta_2,\dots$$

是两组相互独立生成的随机变量。

现在考虑两个事件：

$$A=\{X_{10} = 0\}$$

$$B = \{Y_{10} = 2\}$$

其中 $A$ 是第一坐标事件，$B$ 是第二坐标事件。

所谓第一坐标事件，指的是只由横坐标决定、与纵坐标无关的事件。例如

$$A = \{X_{10} = 0\}$$

只关心横坐标。

因为

$$X_{10} = \epsilon_1 + \epsilon_2 + \cdots + \epsilon_{10}$$

所以 $A$ 只由 $\epsilon_1,\epsilon_2,\dots,\epsilon_{10}$ 决定，与 $\eta_1,\eta_2,\cdots,\eta_{10}$ 无关。

也就是说，不论纵坐标如何变化，只要横坐标在 10 步后回到 0，事件 $A$ 就会发生。

同理，不论横坐标如何变化，只要纵坐标在 10 步后等于 2，事件 $B$ 就会发生。因此 $B$ 是第二坐标事件。

更严格地说，我们可以把横坐标的随机性放在第一个概率空间

$$(\Omega_X, \mathcal{F}_X,\mathbb{P}_X)$$

中，把纵坐标的随机性放在第二个概率空间

$$(\Omega_Y, \mathcal{F}_Y, \mathbb{P}_Y)$$

中。

整个二维随机游走的概率空间就是乘积空间：

$$\Omega = \Omega_X \times \Omega_Y$$

$$\mathcal{F} = \mathcal{F}_X \otimes \mathcal{F}_Y$$

$$\mathbb{P} = \mathbb{P}_X \otimes \mathbb{P}_Y$$

一个样本点写成

$$\omega =(\omega_X, \omega_Y)$$

其中 $\omega_X$ 决定横坐标如何演化，$\omega_Y$ 决定纵坐标如何演化。

于是事件 $A = \{X_{10} = 0\}$ 在乘积空间中实际上是

$$A_X \times \Omega_Y$$

其中 $A_X = \{\omega_X: X_{10} (\omega_X) = 0\}$。

也就是说：

$$\{X_{10} = 0\} = A_X \times \Omega_Y$$

它只限制第一坐标，不限制第二坐标。

同理，事件 $B = \{Y_{10} = 2\}$ 在乘积空间中是

$$\Omega_X \times B_Y$$

其中 $B_Y = \{\omega_Y: Y_{10} (\omega_Y) = 2\}$。

也就是说：

$$\{Y_{10} = 2\} = \Omega_X \times B_Y$$

它只限制第二坐标，不限制第一坐标。

下面证明它们相互独立。

根据乘积测度的定义，对任意

$$A_X \in \mathcal{F}_X, B_Y\in \mathcal{F}_Y$$

都有

$$\mathbb{P}(A_X \times B_Y) = \mathbb{P}_X(A_X) \mathbb{P}_Y(B_Y)$$

而

$$A \cap B = (A_X \times \Omega_Y) \cap (\Omega_X \times B_Y) = A_X \times B_Y$$

所以

$$\mathbb{P}(A \cap B) = \mathbb{P}(A_X \times B_Y)$$

由乘积测度的定义：

$$\mathbb{P}(A \cap B) = \mathbb{P}_X(A_X) \mathbb{P}_Y(B_Y)$$

另一方面，

$$\mathbb{P}(A) = \mathbb{P}(A_X \times \Omega_Y) = \mathbb{P}_X(A_X)\mathbb{P}_Y(\Omega_Y)$$

因为 $\mathbb{P}_Y(\Omega_Y) = 1$，所以 $\mathbb{P}(A) = \mathbb{P}_X(A_X)$。

同理，$\mathbb{P}(B) = \mathbb{P}(\Omega_X \times B_Y) = \mathbb{P}_X(\Omega_X) \mathbb{P}_Y(B_Y) = \mathbb{P}_Y(B_Y)$。

因此

$$\mathbb{P}(A) \mathbb{P}(B) = \mathbb{P}_X(A_X) \mathbb{P}_Y(B_Y)$$

所以

$$\boxed{\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)}$$

这就证明了事件 $\{X_{10} = 0\}$ 与 $\{Y_{10} = 2\}$ 相互独立。


# 向量范数

设 $V$ 是实数域或复数域上的向量空间。一个函数

$$\|\cdot\| : V\to [0, +\infty)$$

称为范数，若它满足以下三个条件。

第一，正定性：

$$\| x\| \ge 0$$

并且

$$\| x \| = 0 \iff x = 0$$

第二，齐次性：

$$\|\alpha x\| = |\alpha|\| x\|$$

第三，三角不等式：

$$\|x + y\| \le \|x\| + \|y\|$$

直观地说，范数可以看作“长度”的抽象推广。

对

$$x = (x_1, x_2, \cdots, x_n) \in \mathbb{R}^n$$

常见范数有：

## $1$-范数

$$\|x\|_1 = \sum_{i=1} ^n |x_i|$$

## $2$-范数

$$\|x\|_2 = \sqrt{\sum_{i = 1}^n |x_i|^2}$$

也就是欧几里得长度。

## 无穷范数

$$\|x\|_{\infty} =\max_i |x_i|$$

也就是向量中绝对值最大的分量。

# 矩阵范数

给定一个向量范数 $\|\cdot\|$，定义矩阵 $A$ 的诱导范数为

$$\|A\| =\sup_{x \ne 0} \frac{\|Ax\|}{\|x\|}$$

等价地，也可以写成：

$$\boxed{\|A\| = \sup_{\|x\| = 1} \|Ax\|}$$

它的含义是：矩阵 $A$ 作为线性变换，最多能把向量长度放大多少倍。

因此，若 $\|A\|=3$，就表示 $A$ 最多能把某些方向上的向量长度放大 3 倍。

## 为什么两个定义等价

我们证明：

$$\sup_{x \ne 0} \frac{\|Ax\|}{\|x\|} = \sup_{\|x\| = 1} \|Ax\|$$

对任意 $x\ne 0$，令

$$u = \frac{x}{\|x\|}$$

那么

$$\|u\| = 1$$

并且

$$Ax = A(\|x\| u) = \|x\| Au$$

所以

$$\frac{\|Ax\|}{\|x\|} = \|Au\|$$

因此，对所有非零 $x$ 取上确界，等价于对所有单位向量 $u$ 取上确界。

所以：

$$\boxed{\|A\| = \sup_{\|x\| = 1}\|Ax\|}$$

设矩阵范数由向量范数诱导出来，则它满足：

## 非负性

$$||A|| \ge 0$$

因为：

$$\frac{||Ax||}{||x||} \ge 0$$

## 正定性

$$||A|| = 0 \iff A = 0$$

证明：

若 $A=0$，显然

$$||A|| = 0$$

反过来，如果

$$||A|| = 0$$

则对任意 $x \ne 0$，有

$$\frac{||Ax||}{||x||} = 0$$

所以：

$$||Ax|| = 0$$

根据向量范数的正定性：

$$Ax = 0$$

对所有$x$都成立，因此：

$$A = 0$$

## 齐次性

$$||\alpha A|| = |\alpha| ||A||$$

证明：

$$||\alpha A|| = \sup_{x \ne 0} \frac{||\alpha Ax||}{||x||} = \sup_{x\ne 0} \frac{|\alpha| ||Ax||}{||x||} = |\alpha| \sup_{x\ne 0} \frac{||Ax||}{||x||}$$

所以：

$$||\alpha A || = |\alpha | ||A||$$


## 三角不等式

$$|| A + B|| \le ||A|| + ||B||$$

证明：

对任意$x\ne 0 $,

$$||(A+B)x|| = ||Ax + Bx||$$

由向量范数的三角不等式：

$$||Ax + Bx|| \le ||Ax|| + ||Bx||$$

又因为诱导范数定义给出：

$$||Ax|| \le ||A|| ||x||$$

$$||Bx|| \le ||B|| ||x||$$

所以：

$$||(A+B)x|| \le (||A|| + ||B||)||x||$$

两边除以 $||x||$：

$$\frac{||(A+B) x||}{||x||} \le ||A|| + ||B||$$

对所有$x \ne 0 $取上确界：

$$||A +B|| \le ||A || +||B||$$

## 次可乘性

矩阵范数最关键的性质：

$$\boxed{||AB|| \le ||A|| ||B||}$$

这叫次可乘性。

证明：

对任意 $x \ne 0$，

$$||ABx|| = ||A(Bx)||$$

由诱导范数定义：

$$||A(Bx)|| \le ||A|| ||Bx||$$

又有：

$$||Bx|| \le ||B|| ||x||$$

所以：

$$||ABx|| \le ||A|| ||B|| ||x||$$

两边除以 $||x||$：

$$\frac{||ABx||}{||x||} \le ||A|| ||B||$$

对所有非零 $x$ 取上确界：

$$\boxed{||AB|| \le ||A|| ||B||}$$

## 矩阵无穷范数的具体公式

如果向量使用无穷范数：

$$||x||_{\infty} = \max_j |x_j|$$

那么对应的诱导范数为：

$$\boxed{||A||_{\infty} = \max_{i} \sum_j |a_{ij}|}$$

也就是矩阵的每一行绝对值之和的最大值。

###  先证明上界


对任意向量 $x$，第 $i$ 个分量为：

$$(Ax)_i = \sum_j a_{ij}x_j$$

于是：

$$|(Ax)_i| = |\sum_j a_{ij} x_j| \le \sum_{j} |a_{ij}| |x_j|$$

因为：

$$|x_j| \le ||x||_{\infty}$$

所以：

$$|(Ax)_i| \le \sum_j |a_{ij}| ||x||_{\infty}$$

即：

$$|(Ax)_i| \le (\sum_j |a_{ij}|) ||x||_{\infty}$$

对所有$i$选取最大值：

$$||Ax||_{\infty} = \max_i |(Ax)_i| \le (\max_i \sum_j |a_{ij}|) ||x||_{\infty}$$

因此：

$$\frac{||Ax||_{\infty}}{||x||_{\infty}} \le \max_i \sum_j |a_{ij}|$$

对所有 $x \ne 0$ 取上确界：

$$||A||_{\infty} \le \max_i \sum_j |a_{ij}|$$

## 证明下界

设第 $k$ 行达到最大行和：

$$\sum_j |a_{kj}| = \max_i \sum_j |a_{ij}|$$

我们构造一个向量 $x$，使得第 $k$ 行的各项贡献同向叠加。

在实数情形下，取：

$$x_j =\left\{\begin{matrix}
1,a_{kj} \ge 0 \\
-1,a_{kj} < 0
\end{matrix}\right.$$

于是：

$$|x_j| = 1$$

所以：

$$||x||_{\infty } = 1$$

并且：

$$(Ax)_k = \sum_j a_{kj}x_j = \sum_j |a_{kj}|$$

因此：

$$||Ax||_{\infty} \ge |(Ax)_k| = \sum_j |a_{kj}| = \max_i \sum_j |a_{ij}|$$

所以：

$$||A||_{\infty} = \sup_{||x||_{\infty } = 1} ||Ax||_{\infty} \ge \max_{i} \sum_j |a_{ij}|$$

结合上界和下界：

$$\boxed{||A||_{\infty} = \max_i \sum_j |a_{ij}|}$$

## 随机矩阵

行随机矩阵满足：
$$R_{ij} \ge 0$$

并且：

$$\sum_j R_{ij} = 1$$

所以：

$$||R||_{\infty} =\max_i \sum_j |R_{ij}| = \max_i \sum_j R_{ij} = 1$$

这就是随机游走转移矩阵的关键性质。

## $||qR||_{\infty} = q$

由齐次性：

$$||qR||_{\infty} = |q| ||R||_{\infty}$$

题目中：

$$0\le q  < 1$$

所以：

$$|q| = q$$

又因为：

$$||R|| _{\infty} =1$$

因此：

$$\boxed{||qR||_{\infty} = q} $$

## $(qR)^t \to 0$

由次可乘性：

$$||(qR)^t||_{\infty} \le (||qR||_{\infty})^t$$

又因为：

$$||qR||_{\infty} = q$$

所以：

$$||(qR)^t||_{\infty} \le q ^ t$$

因为：

$$0 \le q < 1$$

所以：

$$q^t \to 0$$

于是：

$$||(qR)^t||_{\infty} \to 0$$

矩阵范数趋于 0，意味着矩阵趋于零矩阵，所以：

$$\boxed{(qR)^t \to 0}$$

## 为什么矩阵范数趋于0意味着矩阵趋于零矩阵？

以无穷范数为例。

如果

$$||A_n||_{\infty} \to 0$$

那么： 

$$\max_{i} \sum_{j} |(A_n)_{ij}| \to 0$$

由于每个元素都满足：

$$|(A_n)_{ij}| \le \sum_j |(A_n)_{ij}| \le ||A_n||_{\infty}$$

所以：

$$|(A_n)_{ij}| \to 0$$

也就是说，每一个矩阵元素都趋于 $0$。

因此：

$$A_n \to 0$$

# 谱半径

谱半径定义为：

$$\rho(A) = \max_{\lambda \in \sigma (A)} |\lambda|$$

其中 $\sigma(A)$ 是 $A$ 的全部特征值集合。

对任意诱导矩阵范数，都有：

$$\boxed{\rho(A) \le ||A||}$$

证明：

设 $\lambda$ 是 $A$ 的特征值，对应非零特征向量为 $v$，也就是：
$$Av = \lambda v$$

那么：

$$||Av|| = ||\lambda v|| = |\lambda| ||v||$$

另一方面：

$$||Av|| \le ||A|| ||v||$$

所以：

$$|\lambda| ||v|| \le ||A|| ||v|| $$

由于 $v \ne 0$，所以：

$$||v|| > 0$$

两边除以 $||v||$，得到：

$$|\lambda| \le ||A||$$

对所有特征值取最大值：

$$\boxed{\rho (A) \le ||A||}$$

# 矩阵几何级数

设 $A = qR$。

我们想要证明：

$$\sum_{t=0}^\infty A^t = (I-A)^{-1}$$

也就是：

$$I + A + A^2 + A^3 + \cdots = (I-A)^{-1}$$

关键条件是：

$$||A|| < 1$$

## 先看有限部分和

定义：

$$S_N = I + A+ A^2 + \cdots + A^N$$

现在计算： 

$$(I-A) S_N$$

展开：

$$(I-A)S_N = (I-A)(I+A+A^2+ \cdots + A^N)$$

分配律展开：

$$= I + A+A^2 + \cdots + A^N - A - A^2 - A^3 - \cdots - A^{N + 1}$$

中间全部抵消：

$$A - A = 0$$

$$A^2 - A ^ 2 = 0$$

一直抵消到$$A^N$$。

最后只剩下：

$$(I-A) S_N = I - A^{N + 1}$$

所以：

$$\boxed{(I-A)(I+A+\cdots + A^N) = I - A^{N + 1}}$$

同理，因为 $S_N$ 是 $A$ 的多项式，所以它与 $A$ 可交换，也有：

$$S_N(I-A)= I-A^{N + 1}$$

## 为什么可以令$N\to \infty$

如果 $||A|| < 1$，

那么由矩阵范数的次可乘性：

$$||A^{N+ 1}|| \le ||A|| ^{ N+ 1}$$

由于：

$$0\le ||A|| <  1$$

所以：

$$||A|| ^ { N + 1} \to 0$$

于是：

$$||A^{N + 1}|| \to 0$$

也就是：

$$A^{N+1} \to 0$$


因此：

$$I - A^{N+1} \to I$$

## 有限和$S_N$也会收敛

我们还需要知道

$$S_N = I + A + \cdots + A^N$$

本身有极限。

因为对 $M > N$，有：

$$S_M - S_N = A ^ {N + 1} + A^{N + 2} + \cdots + A^M$$

取范数：

$$||S_M - S_N|| \le ||A^{N + 1} || + ||A^{N + 2}|| + \cdots + ||A^M||$$

由次可乘性：

$$||A^k|| \le ||A||^k$$

所以：

$$||S_M - S_N|| \le ||A|| ^{N + 1} + ||A||^{N+2} + \cdots + ||A||^M$$

右边是普通几何级数尾项：

$$\le \frac{||A||^{N + 1}}{1 - ||A||}$$

当 $N \to \infty$ 时：

$$\frac{||A||^{N+1}}{1-||A||} \to 0$$

所以 $S_N$ 是 Cauchy 列，因此收敛。

设：

$$S = \lim_{N\to \infty} S_N$$

也就是：

$$S = \sum_{t=0}^\infty A^t$$

## 对恒等式取极限

前面已有：

$$(I-A)S_N = I- A^{N + 1}$$

令$N\to \infty$。

左边：

$$(I-A)S_N \to (I-A)S$$

右边：

$$(I-A^{N + 1}) \to I$$

所以：

$$(I-A)S =I$$

同理，由

$$S_N(I-A) = I-A^{N + 1}$$

取极限，得：

$$S(I-A) = I$$

因此$S$同时是$I-A$的左逆和右逆。

所以：

$$S=(I-A)^{-1}$$

于是：

$$\boxed{\sum_{t=0} ^\infty A^t = (I-A)^{-1}}$$

代回 $A = qR$，得到：

$$\boxed{\sum_{t=0}^\infty (qR)^t = (I-qR)^{-1}}$$

# Bolzano-Weierstrass定理

常用形式是：

> **任意有界实数列，都存在一个收敛子列。**

也就是说，若 $(x_n)$ 是有界实数列，那么一定可以从里面挑出一串下标：

$$n_1 < n_2 < n_3 < \cdots$$

使得子列 $x_{n_1}, x_{n_2}, x_{n_3}, \cdots$ 收敛到某个实数 $L$。

我们下面用二分区间法来证明。

## 因为数列有界，所以它落在了一个有限区间里

因为 $(x_n)$ 有界，所以存在实数 $a < b$，使得所有项都落在区间 $[a,b]$ 中，即 $x_n \in [a,b]$（$n=1,2,3,\cdots$）。

也就是说，这个无限数列的所有点都被装进了一个有限长度的闭区间 $[a,b]$。

## 把区间一分为二

把 $[a,b]$ 分成左右两个闭区间：

$$[a,\frac{a+b}{2}],[\frac{a+b}{2},b]$$

数列有无穷多项。

这无穷多项分布在两个半区间里。

根据容斥原理：

> 两个盒子装无穷多个数，至少有一个盒子里装了无穷多个数。

所以至少一个半区间包含数列中的无穷多项。

选这个半区间，记为 $I_1$。

于是：$I_1 \subseteq [a,b]$，$I_1$ 包含无穷多个 $x_n$，$I_1$ 的长度是 $\dfrac{b-a}{2}$。

## 不断二分

继续把$I_1$一分为二。 

两个半区间中，至少有一个包含无穷多个数列项。

选这个半区间，记为$I_2$

于是$I_2\subseteq I_1$

并且 $I_2$ 仍然包含无穷多个 $x_n$。

继续这样做，可以得到一串闭区间：

$$I_1 \supseteq I_2 \supseteq I_3 \cdots$$

每个$I_k$都满足：

1.$I_k$是闭区间。

2.$I_k$包含无穷多个数列项。

3. 区间长度为：

$$|I_k| = \frac{b - a}{2^k}$$

所以：

$$|I_k| \to 0$$

## 从这些区间中跳出子列

因为 $I_1$ 包含无穷多个数列项，所以可以选一个下标 $n_1$，使得

$$x_{n_1}\in I_1$$

因为 $I_2$ 也包含无穷多个数列项，所以可以选一个更大的下标：

$$n_2 > n_1$$

使得：

$$x_{n_2}\in I_2$$

这是可以做到的，因为 $I_2$ 里有无穷多个数列项，不可能全部排在 $n_1$ 之前。

同理，可递归选取：

$$n_1 < n_2 < n_3 < \cdots$$

并且：

$$x_{n_k} \in I_k$$

于是我们得到一个子列：

$$x_{n_1},x_{n_2},x_{n_3},\dots$$

## 这些嵌套区间有唯一公共点

设

$$I_k = [a_k, b_k]$$

因为区间嵌套：

$$I_1\supseteq I_2 \supseteq I_3 \supseteq \cdots$$

所以左端点单调递增：

$$a_1 \le a_2 \le a_3 \le \cdots$$

右端点单调递减：

$$b_1 \ge b_2 \ge b_3 \ge \cdots$$

并且对所有 $k$，都有：

$$a_k \le b_k$$

定义：

$$L = \sup \{a_k : k \ge 1\}$$

由于每个 $a_k \le b_k$，并且 $b_k$ 是所有后续左端点的上界，所以可以证明：

$$a_k \le L \le b_k, \forall k$$

因此：

$$L \in I_k, \forall k$$

因此：

$$L \in \bigcap_{k=1}^\infty I_k$$

又因为长度趋于 0：

$$b_k - a_k = |I_k| = \frac{b-a} {2^k} \to 0$$

所以这个公共点只能有一个。

因此：

$$\cap _{k = 1} ^\infty I_k = \{L\}$$

这就是嵌套闭区间定理在这里的应用。

## 证明子列收敛到 $L$

我们已经选出了：

$$x_{n_k}\in I_k$$

同时：

$$L\in I_k$$

所以 $x_{n_k}$ 和 $L$ 都在同一个区间 $I_k$ 里面。

因为它们之间的距离不超过区间长度：

$$|x_{n_k} - L | \le |I_k|$$

而：

$$|I_k| = \frac{b-a}{2^k} \to 0$$

根据夹逼定理：

$$|x_{n_k} - L | \to 0$$

也就是：

$$x_{n_k} \to L$$

因此，从有界数列$(x_n)$中成功选出了一个收敛子列。

这就证明了 Bolzano-Weierstrass 定理。

# 柯西列

数列 $(x_n)$ 是柯西列，意思是：

$$\forall \epsilon > 0,\ \exists N,\ \forall m, n \ge N,\ |x_m - x_n| < \epsilon$$

就是后面的项彼此越来越近。

我们要证明：存在某个实数 $L$，使得

$$x_n \to L$$

## 柯西列一定有界

因为 $(x_n)$ 是柯西列，取

$$\epsilon = 1$$

则存在 $N$，使得 $m,n \ge N$ 时：

$$|x_m - x_n |  < 1$$

特别地，固定 $n=N$，则对所有 $m \ge N$，有：

$$|x_m - x_N| < 1$$

也就是说：

$$x_m \in (x_N - 1, x_N + 1)$$

所以从第$N$项以后，所有项都能被夹在一个有限区间里。

前面有限多个数：

$$x_1,x_2,\cdots, x_{N-1}$$

当然也是有界的。

因此整个数列$(x_n)$有界。

所以：

> **柯西列一定有界。**

## 有界数列存在收敛子列

因为 $(x_n)$ 是有界实数列，根据 Bolzano-Weierstrass 定理，它存在一个收敛子列。

也就是说，存在下标

$$n_1 < n_2 < n_3 < \cdots$$

以及某个实数 $L$，使得：

$$x_{n_k} \to L$$

现在我们已经知道，柯西列至少有一条子列收敛到$L$。

接下来我们证明整个数列都收敛到同一个 $L$。

## 柯西性把整个数列拖向子列极限

给定任意

$$\epsilon > 0$$

因为 $(x_n)$ 是柯西列，所以存在 $N_1$，使得只要

$$m,n \ge N_1$$

就有：

$$|x_m - x_n| < \frac{\epsilon}{2}$$

又因为子列

$$x_{n_k} \to L$$

所以存在 $K$，使得：

$$n_K \ge N_1$$

并且

$$|x_{n_K} - L| < \frac{\epsilon}{2}$$

现在对于任意

$$n \ge N_1$$

根据三角不等式：

$$|x_n - L| \le |x_n - x_{n_K}| + |x_{n_K} - L|$$

因为

$$n \ge N_1,\quad n_K \ge N_1$$

由柯西性：

$$|x_n - x_{n_K}| < \frac{\epsilon}{2}$$

又有：

$$|x_{n_K} - L| < \frac{\epsilon}{2}$$

所以：

$$|x_n - L| < \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon$$

因此：

$$\forall \epsilon > 0,\ \exists N_1,\ \forall n \ge N_1,\ |x_n - L| < \epsilon$$

这正是：

$$x_n \to L$$

所以柯西列收敛。


# 现在终于开始题目了...

设有一张无向连通图

$$G=(V,E)$$

其中

$$V=\{1,2,\cdots,N\}$$

表示 $N$ 个城市，边集 $E$ 表示城市之间的道路。如果城市 $u$ 和城市 $v$ 之间有道路，则记为

$$u \sim v$$

对每个城市 $u$，记其度数为

$$\deg(u) = |\{v \in V: u \sim v\}|$$

臭蛋初始位于城市 $1$。

给定两个正整数 $P,Q$，满足

$$1 \le P \le Q$$

定义爆炸概率为

$$p = \frac{P}{Q}$$

不爆炸概率为

$$q = 1-p = 1-\frac{P}{Q}$$

在每一个离散时刻 $t=0,1,2,\cdots$，若臭蛋当前位于城市 $u$，则执行如下随机过程：

- 以概率 $p$ 爆炸，污染当前城市 $u$，过程终止；
- 以概率 $q$ 不爆炸，并从城市 $u$ 的所有邻居中等概率选取一个城市 $v$ 移动过去。

因此转移概率为

$$\mathbb{P}(u \to v) = \begin{cases}
\dfrac{1}{\deg(u)}, & u \sim v \\
0, & u \not\sim v
\end{cases}$$

然后进入下一个时刻。

定义随机变量 $Z$ 表示最后被污染的城市编号。

求出所有 $i \in V$ 对应的

$$\mathbb{P}(\{\omega: Z(\omega) = i\})$$

也就是每个城市最终被污染的概率。

# 第一维：爆炸判定空间 $\Omega_B$

每个时刻都有一次爆炸判定。记

$$B_t \in \{0,1\}$$

其中 $B_t=1$ 表示第 $t$ 次判定爆炸，$B_t=0$ 表示第 $t$ 次判定不爆炸。

于是，整个爆炸结果可以看成一个无限的 $01$ 序列：

$$b=(b_0,b_1,b_2,\cdots)$$

因此定义爆炸空间为：

$$\boxed{\Omega_B = \{0,1\}^{\mathbb{N}_0}}$$

其中

$$\mathbb{N}_0 = \{0,1,2,\dots\}$$

一个元素

$$b \in \Omega_B$$

就是一条完整的爆炸判定序列。

例如：

$$b=(0,0,1,0,1,\cdots)$$

表示：

- 第 $0$ 次不爆炸；
- 第 $1$ 次不爆炸；
- 第 $2$ 次爆炸；
- 后面的取值实际上已经不会再被用到。

在 $\Omega_B$ 上定义概率测度：

$$\mathbb{P}_B = (q\delta_0 + p\delta_1)^{\otimes \mathbb{N}_0}$$

也就是说：

$$\mathbb{P}_B(B_t = 1) = p,\qquad \mathbb{P}_B(B_t = 0) = q$$

并且

$$B_0,B_1,B_2,\cdots$$

相互独立。

# 第二维：潜在随机游走路径空间 $\Omega_W$

现在描述：如果臭蛋一直没有爆炸，它会如何随机游走。

一条潜在路径是：

$$y = (y_0,y_1,y_2,\cdots)$$

其中

$$y_t \in V$$

并且每一步只能沿边走，因此必须满足

$$y_t \sim y_{t+1},\qquad t=0,1,2,\cdots$$

由于臭蛋初始位于城市 $1$，还要求 $y_0=1$。因此潜在随机游走路径空间为：

$$\boxed{\Omega_W = \left\{y = (y_0,y_1,y_2,\dots) \in V^{\mathbb{N}_0}: y_0=1,\ y_t \sim y_{t+1}\ \forall t \ge 0\right\}}$$

一个元素

$$y \in \Omega_W$$

就是一条从城市 $1$ 出发的无限长合法游走路径。

例如：

$$y=(1,3,4,2,5,7,\cdots)$$

表示：如果一直不爆炸，臭蛋就会沿着这条路径游走。

在 $\Omega_W$ 上定义随机游走路径测度 $\mathbb{P}_W$。

对于任意一条有限合法路径

$$(v_0,v_1,\dots,v_t)$$

其中

$$v_0 = 1,\qquad v_k \sim v_{k+1}$$

定义柱集事件

$$C(v_0,\cdots,v_t) = \{y\in \Omega_W: y_0=v_0,\ldots,y_t=v_t\}$$

它表示潜在随机游走的前 $t$ 步恰好是 $v_0,\ldots,v_t$。其概率定义为：

$$\boxed{\mathbb{P}_W(C(v_0,\cdots,v_t))=\prod_{k=0}^{t-1} \frac{1}{\deg(v_k)}}$$

等价地，若记 $Y_t=y_t$，则

$$\mathbb{P}_W(Y_0=v_0,\ldots,Y_t=v_t)=\prod_{k=0}^{t-1}\frac{1}{\deg(v_k)}$$

这就是普通随机游走的路径概率。

# 总概率测度

整体概率空间取乘积：

$$\Omega = \Omega_B \times \Omega_W,\qquad \mathbb{P} = \mathbb{P}_B \otimes \mathbb{P}_W$$

也就是说，爆炸判定序列与潜在随机游走路径是独立生成的。

因此，对爆炸事件

$$A \subseteq \Omega_B$$

和路径事件

$$C \subseteq \Omega_W$$

有

$$\boxed{\mathbb{P}(A \times C) = \mathbb{P}_B(A)\,\mathbb{P}_W(C)}$$

这就是两个独立维度在概率论中的形式。

# 在这个空间上定义随机变量

对于样本点

$$\omega = (b,y) \in \Omega$$

定义爆炸判定变量：

$$B_t(\omega) = b_t$$

定义潜在随机游走位置：

$$Y_t(\omega) = y_t$$

定义爆炸时间：

$$T(\omega) = \inf\{t \ge 0: b_t = 1\}$$

若永远不爆炸，即

$$b_t = 0,\quad \forall t \ge 0$$

则可记 $T = \infty$。但因为 $p > 0$，所以

$$\mathbb{P}(T < \infty) = 1$$

事实上，

$$\mathbb{P}(T = t) = q^t p,\qquad t = 0,1,2,\ldots$$

最终污染城市定义为

$$Z(\omega) = Y_{T(\omega)}(\omega)$$

当 $T(\omega) < \infty$ 时，这就是爆炸时刻臭蛋所在的城市。

题目要求求出所有 $i \in V$ 对应的

$$\mathbb{P}(\{\omega \in \Omega: Z(\omega) = i\})$$

也就是每个城市最终被污染的概率。

# 两个独立维度

因为

$$T(\omega)=T(b,y)$$

只依赖第一坐标 $b$，而

$$Y_t(\omega)=Y_t(b,y)=y_t$$

只依赖第二坐标 $y$。

更具体地，可写成

$$T(b,y)=T(b),\qquad Y_t(b,y)=y_t$$

因此 $\{T=t\}$ 是第一坐标事件：

$$\{T=t\} = \{b\in \Omega_B: b_0=0,\ldots,b_{t-1}=0,\ b_t=1\} \times \Omega_W$$

而 $\{Y_t=i\}$ 是第二坐标事件：

$$\{Y_t=i\} = \Omega_B \times \{y\in \Omega_W: y_t=i\}$$

由于总概率测度是乘积测度

$$\mathbb{P}=\mathbb{P}_B \otimes \mathbb{P}_W$$

所以第一坐标事件与第二坐标事件相互独立。

因此

$$\boxed{\mathbb{P}(T=t,\ Y_t=i)=\mathbb{P}(T=t)\,\mathbb{P}(Y_t=i)}$$

又因为

$$\mathbb{P}(T=t)=q^t p$$

所以

$$\boxed{\mathbb{P}(T=t,\ Y_t=i)=q^t p\,\mathbb{P}(Y_t=i)}$$

同理，

$$\{T\ge t\}=\{b\in \Omega_B: b_0=0,\ldots,b_{t-1}=0\}\times \Omega_W$$

所以

$$\mathbb{P}(T\ge t)=q^t$$

并且

$$\boxed{\mathbb{P}(T\ge t,\ Y_t=i)=q^t\,\mathbb{P}(Y_t=i)}$$

## 构造模型和真实过程为什么等价？

我们要证明的不是“两个模型的底层 $\omega$ 一样”，而是：两种模型产生的可观测过程同分布。

为此，设 $\Phi$ 为将样本点 $\omega \in \Omega$ 映射为可观测路径的函数。其取值空间 $\mathcal{P}$ 不是 $\mathbb{R}^n$ 之类的普通空间，而是所有有限合法路径构成的集合，即

$$\Phi: \Omega \to \mathcal{P}$$

只需证明

$$\boxed{\Phi_{\mathrm{real}}(\omega) \overset{d}{=} \Phi_{\mathrm{construct}}(\omega)}$$

即：真实过程的可观测过程，与构造模型 $(T,Y)$ 产生的可观测过程同分布。

## 先定义真实过程

真实过程是：

- 初始城市：

$$X_0 = 1$$

在时刻 $t$，若当前位置为 $X_t=u$，则先以概率 $p$ 爆炸。

若爆炸，则过程停止，最终污染城市为 $u$。

若不爆炸，则以概率 $q=1-p$ 继续，并从 $u$ 的邻居中等概率选取一个城市 $v$，令

$$X_{t+1} = v$$

定义真实爆炸时间 $T_{\mathrm{real}}$ 为第一次爆炸发生的时刻。

真实可观测过程为：

$$\Phi_{\mathrm{real}}(\omega) = \bigl(T_{\mathrm{real}}(\omega),\, X_0(\omega),\, X_1(\omega),\, \cdots,\, X_{T_{\mathrm{real}}(\omega)}(\omega)\bigr)$$

它记录的是：

> 什么时候爆炸，以及爆炸前经过的城市序列。

## 再定义构造模型

构造模型中，我们先生成两套独立随机对象。

第一套是爆炸序列：

$$B_0,B_1,B_2$$

其中

$$\mathbb{P}(\{\omega \in \Omega: B_t(\omega) = 1\}) = p$$

$$\mathbb{P}(\{\omega \in \Omega: B_t(\omega) = 0\}) = q$$

并且各个 $B_t$ 相互独立。

定义：

$$T(\omega) = \inf\{t \ge 0: B_t(\omega) = 1\}$$

所以：

$$\mathbb{P}(\{\omega \in \Omega: T(\omega) = t\}) = q^t p$$

第二套是一条普通随机游走路径：

$$Y_0,Y_1,Y_2,\cdots$$

其中：

$$Y_0 = 1$$

并且：

$$\mathbb{P}(Y_{t+1} = v \mid Y_t = u) = \begin{cases}
\dfrac{1}{\deg(u)}, & u \sim v \\
0, & \text{否则}
\end{cases}$$

并且我们规定 $T$ 与整条路径 $(Y_0,Y_1,Y_2,\dots)$ 相互独立。

构造模型的可观测过程为：

$$\Phi_{\mathrm{construct}}(\omega) = \bigl(T(\omega);\, Y_0(\omega),\, Y_1(\omega),\, \cdots,\, Y_{T(\omega)}(\omega)\bigr)$$

最终污染城市为：

$$Z_{\mathrm{construct}}(\omega) = Y_{T(\omega)}(\omega)$$

我们想要证明：

$$\Phi_{\mathrm{real}} \overset{d}{=} \Phi_{\mathrm{construct}}$$

因为可观测过程是一个有限路径，所以只需证明：对任意合法有限路径，两种模型产生它的概率相同。

## 固定一条合法路径

固定整数 $t \ge 0$，以及一条合法路径 $(v_0,v_1,\cdots,v_t)$，满足

$$v_0 = 1,\qquad v_k \sim v_{k+1},\quad k = 0,1,\dots,t-1$$

我们考虑事件

$$\Phi(\omega) = (t;\, v_0,v_1,\cdots,v_t)$$

它表示：前 $t$ 次判定都不爆炸，臭蛋依次经过 $v_0,v_1,\dots,v_t$，并在第 $t$ 次判定爆炸。

## 真实过程产生这条可观测路径的概率

在真实过程中，要观察到

$$(t;\, v_0,v_1,\dots,v_t)$$

必须依次发生以下事件：

- 第 $0$ 次在 $v_0$ 不爆炸，然后从 $v_0$ 走到 $v_1$；
- 第 $1$ 次在 $v_1$ 不爆炸，然后从 $v_1$ 走到 $v_2$；
- $\cdots$
- 第 $t-1$ 次在 $v_{t-1}$ 不爆炸，然后走到 $v_t$；
- 最后在第 $t$ 次于 $v_t$ 爆炸。

所以概率为：

$$\mathbb{P}_{\mathrm{real}}\bigl(\Phi_{\mathrm{real}} = (t;\, v_0,\dots,v_t)\bigr)
= \left[\prod_{k=0}^{t-1} \left(q \cdot \frac{1}{\deg(v_k)}\right)\right] \cdot p$$

$$= q^t p \prod_{k=0}^{t-1} \frac{1}{\deg(v_k)}$$

## 构造模型产生这条可观测路径的概率

在构造模型中，要有

$$\Phi_{\mathrm{construct}} = (t;\, v_0,\dots,v_t)$$

等价于同时发生两件事：

第一，$T = t$；

第二，$Y_0 = v_0,\, Y_1 = v_1,\, \dots,\, Y_t = v_t$。

所以：

$$\mathbb{P}_{\mathrm{construct}}\bigl(\Phi_{\mathrm{construct}} = (t;\, v_0,\dots,v_t)\bigr)
= \mathbb{P}(T=t,\, Y_0=v_0,\,\cdots,\, Y_t=v_t)$$

由于 $T$ 与随机游走路径 $Y$ 相互独立：

$$= \mathbb{P}(T=t) \cdot \mathbb{P}(Y_0=v_0,\,\dots,\, Y_t=v_t)$$

其中 $\mathbb{P}(T=t) = q^t p$。

而随机游走路径概率为：

$$\mathbb{P}(Y_0=v_0,\,\cdots,\, Y_t=v_t) = \prod_{k=0}^{t-1} \frac{1}{\deg(v_k)}$$

因此：

$$\boxed{\mathbb{P}_{\mathrm{construct}}\bigl(\Phi_{\mathrm{construct}} = (t;\, v_0,\dots,v_t)\bigr)
= q^t p \prod_{k=0}^{t-1} \frac{1}{\deg(v_k)}}$$

## 两边完全相同

$$
\begin{aligned}
&\mathbb{P}_{\mathrm{real}}\bigl(\Phi_{\mathrm{real}} = (t;\, v_0,\dots,v_t)\bigr)
= q^t p \prod_{k=0}^{t-1} \frac{1}{\deg(v_k)} \\
&\text{并且}\quad
\mathbb{P}_{\mathrm{construct}}\bigl(\Phi_{\mathrm{construct}} = (t;\, v_0,\dots,v_t)\bigr)
= q^t p \prod_{k=0}^{t-1} \frac{1}{\deg(v_k)} \\
&\text{所以，对任意合法有限路径，都有} \\
&\boxed{\mathbb{P}_{\mathrm{real}}\bigl(\Phi_{\mathrm{real}} = (t;\, v_0,\dots,v_t)\bigr)
= \mathbb{P}_{\mathrm{construct}}\bigl(\Phi_{\mathrm{construct}} = (t;\, v_0,\dots,v_t)\bigr)}
\end{aligned}
$$

# 天意论

随机并不存在；世界早已由底层样本点 $\omega$ 完全确定。

在本题中，样本空间可分解为

$$\Omega = \Omega_B \times \Omega_W$$

其中

$$\Omega_B = \{0,1\}^{\mathbb{N}_0}$$

是所有爆炸判定序列

$$b = (b_0,b_1,b_2,\dots)$$

的集合。这里 $b_t=1$ 表示第 $t$ 次判定爆炸，$b_t=0$ 表示不爆炸。

另一维是

$$\Omega_W = \left\{y = (y_0,y_1,y_2,\dots) \in V^{\mathbb{N}_0}: y_0=1,\ y_t \sim y_{t+1}\ \forall t \ge 0\right\}$$

即从城市 $1$ 出发的所有潜在随机游走路径。

于是底层样本点写作

$$\omega = (b,y)$$

它携带全部随机信息：何时爆炸，以及若一直不爆炸，臭蛋将如何游走。

但实际观测中，一旦爆炸，后续的判定与路径便不再可见。我们看到的不是整个 $\omega$，而只是其对应的有限过程。

定义爆炸时间

$$T(b) = \inf\{t \ge 0: b_t = 1\}$$

及可观测过程

$$\Phi(\omega) = \Phi(b,y) = \bigl(T(b);\, y_0,y_1,\dots,y_{T(b)}\bigr)$$

即

$$\Phi: \Omega \to \mathcal{P}$$

其中 $\Phi(\omega)$ 记录：臭蛋从城市 $1$ 出发，依次经过若干城市，并在第 $T(b)$ 次判定时爆炸。

不同的底层样本点 $\omega$ 可能对应同一可观测过程。例如，两个样本点在爆炸之后的路径可以不同；只要爆炸之前完全相同，观测结果就一致。于是可能出现

$$\omega_1 \ne \omega_2, \qquad \Phi(\omega_1) = \Phi(\omega_2)$$

这说明 $\Phi$ 把底层完整随机结果压缩成了可观测的有限过程。

最终污染城市定义为

$$Z(\omega) = y_{T(b)}$$

若 $\Phi(\omega) = (t;\, v_0,v_1,\dots,v_t)$，则 $Z(\omega)=v_t$。

因此 $Z$ 只依赖于 $\Phi$：存在函数 $h:\mathcal{P}\to V$，使得

$$h(t;\, v_0,v_1,\dots,v_t) = v_t, \qquad Z = h \circ \Phi$$

换言之，一旦知道 $\Phi(\omega)$，便确定了最终污染城市 $Z(\omega)$。

本题中的关系可概括为

$$\omega \longmapsto \Phi(\omega) \longmapsto Z(\omega)$$

其中 $\omega$ 是底层完整随机结构，$\Phi(\omega)$ 是可观测过程，$Z(\omega)$ 是从该过程中读出的最终污染城市。



# 用全概率公式展开答案

对每个城市 $i$，所求概率为

$$ans_i = \mathbb{P}(Y_T = i)$$

对爆炸时刻 $T$ 做全概率分解：

$$ans_i = \sum_{t=0}^{\infty} \mathbb{P}(T=t,\, Y_t=i)$$

由 $T$ 与随机游走路径相互独立，得

$$\mathbb{P}(T=t,\, Y_t=i) = \mathbb{P}(T=t)\,\mathbb{P}(Y_t=i)$$

代入 $\mathbb{P}(T=t)=q^t p$，即得

$$ans_i = \sum_{t=0}^{\infty} q^t p\,\mathbb{P}(Y_t=i)$$

整理后写成

$$\boxed{ans_i = p \sum_{t=0}^{\infty} q^t \mathbb{P}(Y_t=i)}$$

这是概率形式的答案。

# 转化为期望访问次数

通俗地说，可以把 $x_i$ 理解成：在爆炸真正发生之前，随机游走过程平均会在城市 $i$ 接受多少次「是否爆炸」的判定。

严格定义如下。令随机变量

$$N_i(\omega) = \sum_{t=0}^{\infty} \mathbf{1}_{\{T(\omega) \ge t,\, Y_t(\omega)=i\}}$$

其中 $N_i(\omega)$ 表示：在爆炸发生之前，臭蛋在城市 $i$ 一共接受了多少次爆炸判定。

指示函数 $\mathbf{1}_{\{T(\omega)\ge t,\, Y_t(\omega)=i\}}$ 的含义是：第 $t$ 次判定尚未爆炸，且此时臭蛋位于城市 $i$。

逐项展开，可得

$$N_i(\omega) = \mathbf{1}_{\{T(\omega) \ge 0,\, Y_0(\omega)=i\}} + \mathbf{1}_{\{T(\omega) \ge 1,\, Y_1(\omega)=i\}} + \mathbf{1}_{\{T(\omega) \ge 2,\, Y_2(\omega)=i\}} + \cdots$$

令

$$x_i = \mathbb{E}[N_i]$$

代入上式：

$$x_i = \mathbb{E}\left[\sum_{t=0}^{\infty} \mathbf{1}_{\{T(\omega) \ge t,\, Y_t(\omega)=i\}}\right]$$

换言之，求期望就是对 $\omega$ 积分。

由于每一项都是指示函数

$$\mathbf{1}_{\{T(\omega) \ge t,\, Y_t(\omega)=i\}} \in \{0,1\}$$

故 $N_i(\omega) \ge 0$ 对所有 $\omega$ 成立。由 Tonelli 定理，可交换期望与无穷求和：

$$\boxed{\mathbb{E}\left[\sum_{t=0}^{\infty} \mathbf{1}_{\{T(\omega) \ge t,\, Y_t(\omega)=i\}}\right] = \sum_{t=0}^{\infty} \mathbb{E}\bigl[\mathbf{1}_{\{T(\omega) \ge t,\, Y_t(\omega)=i\}}\bigr]}$$

这里无需先验证 $N_i$ 可积，因为 Tonelli 定理对非负函数允许两边取 $+\infty$。

# 指示函数的期望等于事件概率

对任意事件 $A$，有

$$\mathbb{E}[\mathbf{1}_A] = \mathbb{P}(A)$$

因此

$$\mathbb{E}[\mathbf{1}_{\{T(\omega) \ge t,\, Y_t(\omega)=i\}}] = \mathbb{P}(T \ge t,\, Y_t=i)$$

代入即得

$$x_i = \sum_{t=0}^{\infty} \mathbb{P}(T \ge t,\, Y_t=i)$$

这便是在应用 Tonelli 定理后得到的结果。

# 利用独立性继续化简

$T$ 只由爆炸序列决定，$Y_t$ 只由随机游走路径决定，两者相互独立，故

$$\mathbb{P}(T \ge t,\, Y_t=i) = \mathbb{P}(T \ge t)\,\mathbb{P}(Y_t=i)$$

又 $\mathbb{P}(T \ge t) = q^t$，于是

$$x_i = \sum_{t=0}^{\infty} q^t \mathbb{P}(Y_t=i)$$

即

$$\boxed{x_i = \sum_{t=0}^{\infty} q^t \mathbb{P}(Y_t=i)}$$

# 与最终答案的关系

最终在城市 $i$ 爆炸的概率为

$$ans_i = \mathbb{P}(Y_T = i)$$

这里有一个非常直观的解释：如果一次判定发生在城市 $i$，则以概率 $p$ 在该处爆炸。因此，最终在 $i$ 爆炸的概率就是 $p x_i$。下面用全概率公式再严格推导一遍。

仍对 $T$ 做全概率分解：

$$ans_i = \sum_{t=0}^{\infty} \mathbb{P}(T=t,\, Y_t=i)$$

由独立性，

$$\mathbb{P}(T=t,\, Y_t=i) = \mathbb{P}(T=t)\,\mathbb{P}(Y_t=i)$$

代入 $\mathbb{P}(T=t)=q^t p$，得

$$ans_i = p \sum_{t=0}^{\infty} q^t \mathbb{P}(Y_t=i)$$

而前面已求得

$$x_i = \sum_{t=0}^{\infty} q^t \mathbb{P}(Y_t=i)$$

两式对比，即得

$$\boxed{ans_i = p x_i}$$

# 建立线性方程

城市 $i$ 的期望访问次数 $x_i$ 来自两部分。

其一，若 $i=1$，则 $t=0$ 时臭蛋已在城市 $1$，直接贡献

$$[i=1]$$

其二，臭蛋也可能从邻居 $u$ 走到 $i$。若访问城市 $u$ 的期望次数为 $x_u$，则每次位于 $u$ 时：

- 以概率 $q$ 不爆炸；
- 以概率 $\dfrac{1}{\deg(u)}$ 走到邻居 $i$。

因此 $u$ 对 $x_i$ 的贡献为

$$q\,\frac{x_u}{\deg(u)}$$

对所有邻居 $u \sim i$ 求和，得

$$\boxed{x_i = [i=1] + q\sum_{u \sim i} \frac{x_u}{\deg(u)}}$$

移项后，

$$\boxed{x_i - q\sum_{u \sim i} \frac{x_u}{\deg(u)} = [i=1]}$$

这就是关于 $x_1,\dots,x_N$ 的线性方程组。

# 矩阵形式

定义转移矩阵 $R$，其中

$$R_{u,i} = \begin{cases}
\dfrac{1}{\deg(u)}, & u \sim i \\
0, & \text{否则}
\end{cases}$$

即 $R_{u,i}$ 为从 $u$ 一步走到 $i$ 的概率。

令列向量

$$x = (x_1,\dots,x_N)^{\top}, \qquad e_1 = (1,0,\dots,0)^{\top}$$

则上述方程组可写成

$$\boxed{(I - qR^{\top}) x = e_1}$$

其中 $R^{\top}$ 为 $R$ 的转置。解出 $x$ 后，最终答案为

$$ans_i = p x_i$$

以三点图 $V=\{1,2,3\}$ 为例。按

$$R_{u,i}=
\begin{cases}
\dfrac{1}{\deg(u)}, & u \sim i, \\
0, & u \not\sim i
\end{cases}$$

的定义，矩阵 $R$ 可以写成

$$R=
\begin{bmatrix}
0 & \dfrac{[1\sim 2]}{\deg(1)} & \dfrac{[1\sim 3]}{\deg(1)} \\[6pt]
\dfrac{[2\sim 1]}{\deg(2)} & 0 & \dfrac{[2\sim 3]}{\deg(2)} \\[6pt]
\dfrac{[3\sim 1]}{\deg(3)} & \dfrac{[3\sim 2]}{\deg(3)} & 0
\end{bmatrix}.$$

这里 $[u\sim i]$ 是指示函数：若 $u$ 与 $i$ 相邻，则 $[u\sim i]=1$；否则 $[u\sim i]=0$。

由于 $R_{u,i}$ 表示从 $u$ 走到 $i$ 的概率，所以 $R$ 的行表示出发点，列表示到达点。于是转置矩阵为

$$R^{\top}=
\begin{bmatrix}
0 & \dfrac{[2\sim 1]}{\deg(2)} & \dfrac{[3\sim 1]}{\deg(3)} \\[6pt]
\dfrac{[1\sim 2]}{\deg(1)} & 0 & \dfrac{[3\sim 2]}{\deg(3)} \\[6pt]
\dfrac{[1\sim 3]}{\deg(1)} & \dfrac{[2\sim 3]}{\deg(2)} & 0
\end{bmatrix}.$$

令

$$x=
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}.$$

则

$$(R^{\top}x)_1
= \frac{[2\sim 1]}{\deg(2)}x_2 + \frac{[3\sim 1]}{\deg(3)}x_3
= \sum_{u \sim 1}\frac{x_u}{\deg(u)}.$$

同理，

$$(R^{\top}x)_2
= \frac{[1\sim 2]}{\deg(1)}x_1 + \frac{[3\sim 2]}{\deg(3)}x_3
= \sum_{u \sim 2}\frac{x_u}{\deg(u)},$$

$$(R^{\top}x)_3
= \frac{[1\sim 3]}{\deg(1)}x_1 + \frac{[2\sim 3]}{\deg(2)}x_2
= \sum_{u \sim 3}\frac{x_u}{\deg(u)}.$$

因此，对任意点 $i$，都有统一形式

$$(R^{\top}x)_i = \sum_{u \sim i}\frac{x_u}{\deg(u)}.$$

所以

$$\bigl((I-qR^{\top})x\bigr)_i
= x_i - q(R^{\top}x)_i
= x_i - q\sum_{u \sim i}\frac{x_u}{\deg(u)}.$$

于是矩阵方程

$$(I-qR^{\top})x = e_1$$

等价于线性方程组

$$x_i - q\sum_{u \sim i}\frac{x_u}{\deg(u)} = [i=1],
\qquad i=1,2,3.$$

这正是期望访问次数的递推方程。

# 解的存在性与唯一性

$R$ 为行随机矩阵，故

$$||R||_\infty = 1$$

又由 $0 \le q < 1$，得

$$||qR||_\infty = q < 1$$

于是矩阵几何级数收敛：

$$\sum_{t=0}^{\infty} (qR)^t = (I-qR)^{-1}$$

因此 $I-qR$ 可逆。两边取转置，

$$(I-qR)^{\top} = I - qR^{\top}$$

故 $I-qR^{\top}$ 也可逆。

所以线性方程组

$$(I-qR^{\top})x = e_1$$

存在唯一解。

# 解题代码

```cpp
#include <bits/stdc++.h>
using namespace std;

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    long double P, Q;

    cin >> n >> m >> P >> Q;

    long double p = P / Q;
    long double q = 1.0L - p;

    vector<pair<int, int>> edges;
    vector<int> deg(n + 1);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        edges.push_back({u, v});
        deg[u]++;
        deg[v]++;
    }

    vector<vector<long double>> a(n + 1, vector<long double>(n + 2, 0));

    for (int i = 1; i <= n; i++) {
        a[i][i] = 1.0L;
    }

    a[1][n + 1] = 1.0L;

    for (auto [u, v] : edges) {
        a[v][u] -= q /deg[u];
        a[u][v] -= q /deg[v];
    }


    const long double EPS = 1e-18L;

    for (int col = 1; col <= n; col++) {
        int pivot = col;

        for (int row = col + 1; row <= n; row++) {
            if (fabsl(a[row][col]) > fabsl(a[pivot][col])) {
                pivot = row;
            }
        }
        swap(a[col], a[pivot]);


        if (fabsl(a[col][col]) < EPS) {
            continue;
        }

        long double div = a[col][col];

        for (int j = col; j <= n + 1; j++) {
            a[col][j] /= div;
        }

        for (int row = 1; row <= n; row++) {
            if (row == col) {
                continue;
            }

            long double factor = a[row][col];

            if (fabsl(factor) < EPS) continue;

            for (int j = col; j <= n + 1; j++) {
                a[row][j] -= factor * a[col][j];
            }
        }
    }

    vector<long double> x(n + 1);

    for (int i = 1; i <= n ;i++) {
        x[i] = a[i][n + 1];
    }

    cout << fixed << setprecision(10);

    for (int i = 1; i <= n; i++) {
        long double ans = p * x[i];
        cout << (double)ans << "\n";
    }
    return 0;
}
```

# 复杂度分析

- **建矩阵**：$O(n+m)$。每条边只更新一次增广矩阵中的两个位置。
- **高斯消元**：$O(n^3)$。对 $n$ 个未知数做带部分主元的消元。
- **空间**：$O(n^2)$。存一个 $(n+1)\times(n+2)$ 的增广矩阵。

若题目数据范围较小（例如 $n \le 500$），$O(n^3)$ 的朴素高斯消元完全足够。若 $n$ 很大（例如 $10^5$ 量级），$O(n^3)$ 在时间和 $O(n^2)$ 空间上都无法接受，就不能再用朴素消元——此时应利用方程组的稀疏结构（每个城市 $i$ 的方程只涉及 $i$ 本身及其邻居），改用迭代法、稀疏 LU 分解等方法求解。