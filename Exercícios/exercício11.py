larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt
tinta = area * 0.5

print('\nSua parede tem a dimensão de {} x {} e sua área é de {}m².\nPara pintar essa parede, você precisará de {:.1f}L de tinta.\n'.format(larg, alt, area, tinta))