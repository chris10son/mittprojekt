# Tenta � Projekt                                                                                	Jesper Christenson
                                                                                   	                  	Dev-ops Nackademin
                                                                                                        	2018-09-28
 
 
- V�ldokumenterat / syftet med l�sningen
- Interaktivitet.
- Det skall vara genomtestat / fels�kt.
- Grupp(Max 3 pers, alt ensam)

	Ett "bitcoin" program d�r du kan logga in / registrera dig. 
	Du skall kunna g�ra transaktioner till andra anv�ndare med dina "bitcoins".
	Anv�ndare tilldelas 3 coins vid registrering.
	
Id�e:
Jag vill skapa ett program d�r man som ny anv�ndare kan registrera sig och sedan logga in.
N�r man v�l �r inloggad s� skall man kunna f�ra �ver ett v�rde fr�n sin anv�ndare till en annan existerande anv�ndare.
 
Utf�rande:
Input och fr�ga anv�ndare om de �r anv�ndare sedan innan, eller om de vill bli anv�ndare.
 
Om anv�ndare �r registrerad sedan innan, f�r den f�rs�ka logga in.
Jag testade mig fram och lyckades g�ra en loop som s�kte igenom min .txt fil f�r att se ifall anv�ndare existerar.
Ifall anv�ndar-id eller password �r fel, f�r personen f�rs�ka igen.
 
Om anv�ndare inte �r registrerad f�r anv�ndare fr�gan om de vill registrera sig eller inte
 
Om anv�ndare svarar 'No', avlutas programmet.
 
Om anv�ndare svarar 'Yes'. Skriver vi in det nytt  anv�ndarnamn, l�senord samt ge ny anv�ndare 3 BitJespercoins till att b�rja med. Detta skrivs in i min .txt fil.
N�r detta �r klart h�nvisas anv�ndare till att logga in.
 
N�r anv�ndaren v�l �r inloggad dyker fr�gan upp om de vill �verf�ra pengar till en annan anv�ndare.
skriver anv�ndaren 'No'  printas det  ut �good boy�.
skriver anv�ndaren �Yes� s� f�r anv�ndaren skriva in username hos personen den vill f�ra �ver pengar till.
N�r anv�ndarnamnet v�l skrivits in s�ker programmet igenom ifall username har ett l�senord (som man f�r v�lja n�r man registrerar sig). Om det inte finns ett l�senord hos det angivna username som anv�ndare skrev in s�ger programmet till att det inte finns en s�dan anv�ndare och att han f�r f�rs�ka igen.
F�r att testa detta finns det en anv�ndare under namnet �monalisa� som ej har ett l�senord som du kan f�rs�ka �verf�ra pengar till.
 
Om anv�ndare finns, �verf�rs pengar och det kommer en utskrift p� personens nya balance.


 
 
 
 
