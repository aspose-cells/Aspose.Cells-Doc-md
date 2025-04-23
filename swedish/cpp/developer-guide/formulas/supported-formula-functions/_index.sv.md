---
title: Stödda Excel funktioner med C++
linktitle: Stödda Excel funktioner
type: docs
weight: 10
url: /sv/cpp/supported-formula-functions/
description: Stödda Excel funktioner för att läsa, ställa in och beräkna formler med Aspose.Cells och C++.
keywords: formelfunktion beräkna
---

{{% alert color="primary" %}}

Aspose.Cells API:er stöder de flesta standardfunktioner och inbyggda Excel-formler. Nedan hittar du alla stödda funktioner i alfabetisk ordning.

| | | | | | | | | | | | | |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **[A](#a)** | **[B](#b)** | **[C](#c)** | **[D](#d)** | **[E](#e)** | **[F](#f)** | **[G](#g)** | **[H](#h)** | **[I](#i)** | **[J](#j)** | **[K](#k)** | **[L](#l)** | **[M](#m)** |
| **[N](#n)** | **[O](#o)** | **[P](#p)** | **[Q](#q)** | **[R](#r)** | **[S](#s)** | **[T](#t)** | **[U](#u)** | **[V](#v)** | **[W](#w)** | **[X](#x)** | **[Y](#y)** | **[Z](#z)** |

{{% /alert %}}

Aspose.Cells Formelberäkningsmotor låter dig ange, läsa och beräkna resultaten av följande formler och funktioner.

###### **A**
|**Funktion**|**Sammanfattning**|
| :- | :- |
|ABS|**Matematik och trigonometri**: Returnerar absolutvärdet av ett tal
|ACCRINT|**Ekonomi**: Returnerar intjänad ränta för en säkerhet som betalar periodisk ränta
|ACCRINTM|**Ekonomi**: Returnerar intjänad ränta för en säkerhet som betalar ränta vid förfall
|ACOS|**Matematik och trigonometri**: Returnerar arcuscosinus av ett tal
|ACOSH|**Matematik och trigonometri**: Returnerar den inversa hyperboliska cosinus av ett tal
|ADDRESS|**Sökning och referens**: Returnerar en hänvisning som text till en enda cell i ett kalkylblad
|AGGREGATE|**Matematik och trigonometri**: Returnerar en sammanställning i en lista eller databas
|AMORDEGRC|**Ekonomi**: Returnerar avskrivningen för varje redovisningsperiod genom att använda en avskrivningskoefficient
|AMORLINC|**Ekonomi**: Returnerar avskrivningen för varje redovisningsperiod
|ANCHORARRAY|**Sökning och referens**: Returnerar hela påverkade området för den dynamiska matrisen i cellen
|AND|**Logisk**: Returnerar SANT om alla argument är SANT
|AREAS|**Sökning och referens**: Returnerar antalet områden i en referens
|ARRAYTOTEXT|**Text**: Returnerar en array av textvärden från ett specificerat område
|ASC|**Text**: Ändrar fullbredd (dubbelfel) engelska bokstäver eller katakana inom en teckensträng till halvbredd (enkelbyte) tecken
|ASIN|**Matematik och trigonometri**: Returnerar arcsin för ett nummer
|ASINH|**Matematik och trigonometri**: Returnerar den invektiva hyperboliska sinusen för ett nummer
|ATAN|**Matematik och trigonometri**: Returnerar arctangenten för ett nummer
|ATAN2|**Matematik och trigonometri**: Returnerar arctangenten från x- och y-koordinaterna
|ATANH|**Matematik och trigonometri**: Returnerar den invektiva hyperboliska tangensen för ett nummer
|AVEDEV|**Statistisk**: Returnerar genomsnittet av absoluta avvikelser från data punkter från deras medelvärde
|AVERAGE|**Statistisk**: Returnerar genomsnittet av sina argument
|AVERAGEA|**Statistisk**: Returnerar genomsnittet av sina argument, inklusive nummer, text och logiska värden
|AVERAGEIF|**Statistisk**: Returnerar medelvärdet (aritmetiskt medelvärde) av alla celler i en omfattning som uppfyller ett givet kriterium
|AVERAGEIFS|**Statistisk**: Returnerar medelvärdet (aritmetiskt medelvärde) av alla celler som uppfyller flera kriterier.

###### **B**
|**Funktion**|**Sammanfattning**|
| :- | :- |
|BESSELI|**Teknik**: Returnerar ändrad Bessel-funktion In(x)
|BESSELJ|**Teknik**: Returnerar Bessel-funktion Jn(x)
|BESSELK|**Teknik**: Returnerar ändrad Bessel-funktion Kn(x)
|BESSELY|**Teknik**: Returnerar Bessel-funktion Yn(x)
|BETADIST|**Kompatibilitet**: Returnerar betakumulativ fördelning
|BETA.DIST|**Statistisk**: Returnerar betakumulativ fördelning
|BETAINV|**Kompatibilitet**: Returnerar den invektiva kumulativa fördelningsfunktionen för en specificerad betafördelning
|BETA.INV|**Statistisk**: Returnerar den invektiva kumulativa fördelningsfunktionen för en specificerad betafördelning
|BIN2DEC|**Teknik**: Konverterar ett binärt tal till decimal
|BIN2HEX|**Teknik**: Konverterar ett binärt tal till hexadecimal
|BIN2OCT|**Teknik**: Konverterar ett binärt tal till oktal
|BINOMDIST|**Kompatibilitet**: Returnerar den individuella termen binomialfördelnings sannolikhet
|BINOM.DIST|**Statistisk**: Returnerar den individuella termen binomialfördelnings sannolikhet
|BITAND|**Teknik**: Returnerar ett 'Bitwise And' av två nummer
|BITLSHIFT|**Engineering**: Returnerar ett värde nummer skiftat vänster av shift_amount bitar
|BITOR|**Engineering**: Returnerar en bitvis ELLER av 2 nummer
|BITRSHIFT|**Engineering**: Returnerar ett värde numret skiftad höger med shift_amount bitar
|BITXOR|**Engineering**: Returnerar en bitvis 'Exklusiv Eller' av två nummer
|BYCOL|**Logik**: Tillämpa en LAMBDA på varje kolumn och returnera en array av resultaten
|BYROW|**Logik**: Tillämpa en LAMBDA på varje rad och returnera en array av resultaten

###### **C**
|**Funktion**|**Sammanfattning**|
| :- | :- |
|CEILING|**Kompatibilitet**: Avrundar ett tal till närmaste heltal eller till närmaste multipel av signifikans
|CEILING.MATH|**Matematik och trigonometri**: Avrundar ett tal uppåt, till närmaste heltal eller till närmaste multipel av signifikans
|CEILING.PRECISE|**Matematik och trigonometri**: Avrundar ett tal närmaste heltal eller till närmaste multipel av signifikans. Oavsett talets tecken, avrundas talet uppåt.
|CELL|**Information**: Returnerar information om formatering, plats eller innehåll i en cell
|CHAR|**Text**: Returnerar tecknet som specificeras av kodnumret
|CHIDIST|**Kompatibilitet**: Returnerar sannolikheten för den en-sidiga chi-fördelningen
|CHIINV|**Kompatibilitet**: Returnerar inversen för den en-sidiga sannolikheten av chi-fördelningen
|CHITEST|**Kompatibilitet**: Returnerar testet för oberoende
|CHISQ.DIST|**Statistisk**: Returnerar den kumulativa betasannolikhetsdensiteten
|CHISQ.DIST.RT|**Statistisk**: Returnerar sannolikheten för den en-sidiga chi-fördelningen
|CHISQ.INV.RT|**Statistisk**: Returnerar inversen för den en-sidiga sannolikheten av chi-fördelningen
|CHISQ.TEST|**Statistisk**: Returnerar testet för oberoende
|CHOOSE|**Slå upp och referens**: Väljer ett värde från en lista med värden
|CHOOSECOLS|**Slå upp och referens**: Returnerar de angivna kolumnerna från en array
|CHOOSEROWS|**Slå upp och referens**: Returnerar de angivna raderna från en array
|CLEAN|**Text**: Tar bort alla icke-utskriftsbara tecken från texten
|CODE|**Text**: Returnerar en numerisk kod för den första tecknet i en textsträng
|COLUMN|**Slå upp och referens**: Returnerar kolumnnumret för en referens
|COLUMNS|**Slå upp och referens**: Returnerar antalet kolumner i en referens
|COMBIN|**Matematik och trigonometri**: Returnerar antalet kombinationer för ett givet antal objekt
|COMPLEX|**Engineering**: Konverterar reella och imaginära koefficienter till ett komplext tal
|CONCAT|**Text**: Kombinerar texten från flera intervall och/eller strängar, men den tillhandahåller inte avgränsar- eller Ignoreratom argument
|CONCATENATE|**Text**: Sätter ihop flera textobjekt till ett textobjekt
|CONFIDENCE|**Kompatibilitet**: Returnerar konfidensintervallet för ett populationsmedelvärde
|CONFIDENCE.NORM|**Statistisk**: Returnerar konfidensintervallet för ett populationsmedelvärde
|CONVERT|**Ingenjörskonst**: Omvandlar ett tal från ett mätsystem till ett annat
|CORREL|**Statistisk**: Returnerar korrelationskoefficienten mellan två datamängder
|COS|**Matematik och trigonometri**: Returnerar cosinus för ett tal
|COSH|**Matematik och trigonometri**: Returnerar den hyperboliska cosinus för ett tal
|COUNT|**Statistisk**: Räknar hur många tal som finns i listan med argument
|COUNTA|**Statistisk**: Räknar hur många värden som finns i listan med argument
|COUNTBLANK|**Statistisk**: Räknar antalet blanka celler inom ett intervall
|COUNTIF|**Statistisk**: Räknar antalet celler inom ett intervall som uppfyller de angivna kriterierna
|COUNTIFS|**Statistisk**: Räknar antalet celler inom ett intervall som uppfyller flera kriterier
|COUPDAYBS|**Finansiell**: Returnerar antalet dagar från början av kupongperioden till avvecklingsdagen
|COUPDAYS|**Finansiell**: Returnerar antalet dagar i kupongperioden som innehåller avvecklingsdagen
|COUPDAYSNC|**Finansiell**: Returnerar antalet dagar från avvecklingsdagen till nästa kupongdag
|COUPNCD|**Finansiell**: Returnerar nästa kupongdag efter avvecklingsdagen
|COUPNUM|**Finansiell**: Returnerar antalet kuponger som ska betalas mellan avvecklingsdagen och förfallodagen
|COUPPCD|**Finansiell**: Returnerar den föregående kupongdagen före avvecklingsdagen
|COVAR|**Kompatibilitet**: Returnerar kovarians, genomsnittet av produkterna av parvisa avvikelser
|COVARIANCE.P|**Statistisk**: Returnerar kovarians, genomsnittet av produkterna av parvisa avvikelser
|COVARIANCE.S|**Statistisk**: Returnerar provkovariansen, genomsnittet av produkternas avvikelser för varje datapunktpar i två datamängder
|CRITBINOM|**Kompatibilitet**: Returnerar det minsta värdet för vilket den kumulativa binomialfördelningen är mindre än eller lika med ett kriterievärde
|CUMIPMT|**Finansiell**: Returnerar den kumulativa räntan som betalas mellan två perioder
|CUMPRINC|**Finansiell**: Returnerar den kumulativa huvudstolen som betalas på ett lån mellan två perioder

###### **D**
|**Funktion**|**Sammanfattning**|
| :- | :- |
|DATE|**Datum och tid**: Returnerar serienumret för ett specifikt datum
|DATEDIF|**Datum och tid**: Beräknar antalet dagar, månader eller år mellan två datum. Denna funktion är användbar i formler där du behöver beräkna en ålder.
|DATEVALUE|**Datum och tid**: Konverterar ett datum i form av text till ett serienummer
|DAVERAGE|**Databas**: Returnerar genomsnittet av valda databasposter
|DAY|**Datum och tid**: Konverterar ett serienummer till en dag i månaden
|DAYS|**Datum och tid**: Returnerar antalet dagar mellan två datum
|DAYS360|**Datum och tid**: Beräknar antalet dagar mellan två datum baserat på ett 360-dagars år
|DB|**Finansiell**: Returnerar avskrivningen av en tillgång för en angiven period genom att använda metoden för fastsatt-degressivt saldo
|DCOUNT|**Databas**: Räknar cellerna som innehåller nummer i en databas
|DCOUNTA|**Databas**: Räknar icke-tomma celler i en databas
|DDB|**Ekonomi**: Returnerar avskrivningen av en tillgång under en angiven period genom att använda dubbel minskande balansmetoden eller någon annan metod som du specifierar
|DEC2BIN|**Teknik**: Konverterar ett decimaltal till binärt
|DEC2HEX|**Teknik**: Konverterar ett decimaltal till hexadecimalt
|DEC2OCT|**Teknik**: Konverterar ett decimaltal till oktalt
|DEGREES|**Matematik och trigonometri**: Konverterar radianer till grader
|DELTA|**Teknik**: Testar om två värden är lika
|DEVSQ|**Statistisk**: Returnerar summan av kvadraten på avvikelserna
|DGET|**Databas**: Extraherar från en databas en enskild post som matchar de angivna kriterierna
|DISC|**Ekonomi**: Returnerar rabattsatsen för en säkerhet
|DMAX|**Databas**: Returnerar det maximala värdet från valda databasposter
|DMIN|**Databas**: Returnerar det minsta värdet från valda databasposter
|DOLLAR|**Text**: Konverterar ett nummer till text med formatet $ (dollarvaluta)
|DOLLARDE|**Ekonomi**: Konverterar ett dollapris, uttryckt som en bråkdel, till ett dollapris uttryckt som ett decimaltal
|DOLLARFR|**Ekonomi**: Konverterar ett dollapris, uttryckt som ett decimaltal, till ett dollapris uttryckt som en bråkdel
|DPRODUCT|**Databas**: Multipliserar värdena i ett särskilt fält av poster som matchar kriterierna i en databas
|DROP|**Uppslag och referens**: utesluter ett specificerat antal rader eller kolumner från början eller slutet av en array
|DSTDEV|**Databas**: Beräknar standardavvikelsen baserat på ett urval av valda databasposter
|DSTDEVP|**Databas**: Beräknar standardavvikelsen baserat på hela populationen av valda databasposter
|DSUM|**Databas**: Adderar siffrorna i fältkolumnen för poster i databasen som matchar kriterierna
|DURATION|**Ekonomi**: Returnerar den årliga löptiden för en säkerhet med periodiska räntebetalningar
|DVAR|**Databas**: Beräknar variansen baserad på ett urval av valda databasposter
|DVARP|**Databas**: Beräknar variansen baserad på hela populationen av valda databasposter

###### **E**
|**Funktion**|**Sammanfattning**|
| :- | :- |
|EDATE|**Datum och tid**: Returnerar serienumret för datumet som är det angivna antalet månader före eller efter startdatumet
|EFFECT|**Ekonomi**: Returnerar den effektiva årliga räntesatsen
|ENCODEURL|**Webb**: Returnerar en URL-kodad sträng
|EOMONTH|**Datum och tid**: Returnerar serienumret för den sista dagen i månaden före eller efter ett angivet antal månader
|ERF|**Teknik**: Returnerar felet
|ERFC|**Teknik**: Returnerar det komplementära felet
|ERROR.TYPE|**Information**: Returnerar ett nummer som motsvarar en felfelstyp
|EVEN|**Matematik och trigonometri**: Avrundar ett nummer upp till närmaste jämnt heltal
|EXACT|**Text**: Kontrollerar om två textvärden är identiska
|EXP|**Matematik och trigonometri**: Returnerar e upphöjt till kraften av ett angivet nummer
|EXPONDIST|**Kompatibilitet**: Returnerar den exponentiella fördelningen

###### **F**
|**Funktion**|**Sammanfattning**|
| :- | :- |
|FACT|**Matematik och trigonometri**: Returnerar fakulteten av ett nummer
|FACTDOUBLE|**Matematik och trigonometri**: Returnerar dubbel fakulteten av ett nummer
|FALSE|**Logisk**: Returnerar det logiska värdet FALSKT
|F.DIST|**Statistisk**: Returnerar F-sannolikhetsfördelningen
|FDIST|**Kompatibilitet**: Returnerar F-sannolikhetsfördelningen
|F.DIST.RT|**Statistisk**: Returnerar F-sannolikhetsfördelningen
|FILTER|**Sökning och referens**: Filtrerar en datamängd baserat på de kriterier du definierar
|FIND|**Text**: Hittar en textvärde inom en annan (skiftlägeskänslig)
|FINDB|**Text**: Hittar en textvärde inom en annan (skiftlägeskänslig)
|F.INV.RT|**Statistisk**: Returnerar inversen av F-sannolikhetsfördelningen
|FINV|**Kompatibilitet**: Returnerar inversen av F-sannolikhetsfördelningen
|FISHER|**Statistisk**: Returnerar fischertransformationen
|FISHERINV|**Statistisk**: Returnerar inversen av fischertransformationen
|FIXED|**Text**: Formaterar ett nummer som text med ett fast antal decimaler
|FLOOR|**Kompatibilitet**: Avrundar ett nummer nedåt mot noll
|FLOOR.MATH|**Matematik och trigonometri**: Avrundar ett nummer nedåt till närmaste heltal eller till närmaste multipel av signifikans
|FORECAST|**Statistisk**: Returnerar ett värde längs en linjär trend (I Excel 2016 ersätts denna funktion med FORECAST.LINEAR som en del av de nya prognosfunktionerna)
|FORECAST.LINEAR|**Statistisk**: Returnerar ett framtida värde baserat på befintliga värden
|FORMULATEXT|**Sökning och referens**: Returnerar formeln vid det angivna referens som text
|FREQUENCY|**Statistisk**: Returnerar en frekvensfördelning som en vertikal array
|FV|**Finansiell**: Returnerar det framtida värdet av en investering
|FVSCHEDULE|**Finansiell**: Returnerar det framtida värdet av en ursprunglig huvudsumma efter tillämpning av en serie av räntesatser med sammansatt ränta

###### **G**
|**Funktion**|**Sammanfattning**|
| :- | :- |
|GAMMA.DIST|**Statistisk**: Returnerar gammadistributionen
|GAMMADIST|**Kompatibilitet**: Returnerar gammafördelningen
|GAMMA.INV|**Statistisk**: Returnerar inverteringen av den kumulativa gammafördelningen
|GAMMAINV|**Kompatibilitet**: Returnerar inverteringen av den kumulativa gammafördelningen
|GAMMALN|**Statistisk**: Returnerar den naturliga logarithmen av gammafunktionen, ��(x)
|GCD|**Matematik och trigonometri**: Returnerar största gemensamma delaren
|GEOMEAN|**Statistisk**: Returnerar det geometriska medelvärdet
|GESTEP|**Ingenjörsvetenskap**: Testar om ett tal är större än ett tröskelvärde
|GETPIVOTDATA|**Sökning och referens**: Returnerar data lagrad i en Pivottabellrapport
|GROW
