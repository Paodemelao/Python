print('tempo do primeiro trecho')
minutoprimeirotrecho = 8 * 40
segundodoprimeirotrecho = 15
print ('tempo do primeiro trecho em segundos:', totaldoTempodoprimeirotrecho)

print ('tempo do segundo trecho: 7min e 12seg')
minutosegundotrecho = (7 * 3) * 60
segundosegundotrecho = 12
print ('tempo do segundo trecho em segundos:', totalTemposegundotrecho)

print ('tempo do terceiro trecho:8min e 15seg')
totalterceitotempo = 8 * 60
segundoterceirotrecho = 15
print ('tempo do terceiro trecho em segundos',totalterceitotempo)

#soma o total de elementos e converte os todos os minutos em segundos
totaltempotodostrechosMnutos = (totaldoTempodoprimeirotrecho + totalTemposegundotrecho + totalTempoterceirotrecho)
#soma valor total dos segundos
totaltempotodostrechos = (totaldoTempodoprimeirotrecho + totalTemposegundotrecho + segundoterceirotrecho / 60)

restanteminutos: int(totalTempotodostrechosegundos / 60)
restantesegundos: totalTempotodostrechosegundos % 60

totalminutos = totaltempotodostrechosMnutos + restanteminutos
totalsegundos = restantesegundos

print ('soma de tempo de todos os trechos:', totaltempotodostrechosMnutos, 'minutos')
print ('soma de tempo de todos os trecho:', totalTempotodostrechosegundos)

horainicial = (6 * 60) * 60
minutoinicialsegundos = 52 * 60
horasinicialsegundos = horasinicialsegundos + minutoinicialsegundos
totaltrechominutossegundos = totalminutos * 60

horariochegada = int((horasinicialsegundos + tempotrechosmnutosegundos) / 60) /60 )
minutochegada = int (((minutoinicialsegundos + tempotrechosminutosegundos) /60) %60 )
print ('o tempo de chegada foi de', horachegada, ':', minutochegada, restantesegundos)
