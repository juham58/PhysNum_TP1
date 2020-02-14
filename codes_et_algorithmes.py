
protons = np.random.normal(240, 3, 10000)

def trapezes_pour_hist(f, a, b, N):
    x = np.linspace(a,b,N+1) # N+1 parce que Python commence à indexer à 0
    y = f(x)
    y_droit = y[1:] # points droits du trapèze
    y_gauche = y[:-1] # points gauches du trapèze
    h = (b - a)/N # Largeur des tranches
    I = (h/2) * np.sum(y_droit + y_gauche) # Résultat
    return I

trapezes_pour_hist_eau = lambda x: trapezes_pour_hist(S_col_eau, 3, x, 10240)
trapezes_pour_hist_os = lambda x: trapezes_pour_hist(S_col_os, 3, x, 10240)
trapezes_pour_hist_eau_v = np.vectorize(trapezes_pour_hist_eau)
trapezes_pour_hist_os_v = np.vectorize(trapezes_pour_hist_os)

%timeit -r1 -n1 R_CSDA_trapezes_eau = list(map(trapezes_pour_hist_eau, protons))
#%timeit -r1 -n1 R_CSDA_trapezes_eau_v = trapezes_pour_hist_eau_v(protons)
%timeit -r1 -n1 R_CSDA_trapezes_os = list(map(trapezes_pour_hist_os, protons))
#%timeit -r1 -n1 R_CSDA_trapezes_os_v = trapezes_pour_hist_os_v(protons)


plt.figure(figsize=(16,8))
plt.hist(list(map(trapezes_pour_hist_eau, protons)), 600)


plt.figure(figsize=(16,8))
plt.hist(list(map(trapezes_pour_hist_os, protons)), 600)

plt.show()





quad_pour_hist_eau = lambda x: integrate.quad(S_col_eau, 3, x, epsabs=1e-9)
quad_pour_hist_os = lambda x: integrate.quad(S_col_os, 3, x, epsabs=1e-9)


R_CSDA_quad_eau = list(map(quad_pour_hist_eau, protons))
R_CSDA_quad_os = list(map(quad_pour_hist_os, protons))

plt.figure(figsize=(16,8))
plt.hist(R_CSDA_quad_eau, 600)

plt.figure(figsize=(16,8))
plt.hist(R_CSDA_quad_os, 600)

plt.show()