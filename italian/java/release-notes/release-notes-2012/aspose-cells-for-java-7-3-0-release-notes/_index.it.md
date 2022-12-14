---
title: Aspose.Cells for Java 7.3.0 Note di rilascio
type: docs
weight: 50
url: /it/java/aspose-cells-for-java-7-3-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 7.3.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-7.3.0/)

{{% /alert %}} 

Noi siamo
 felice di annunciare Aspose.Cells for Java v7.3.0!

 Cosa c'è di nuovo

- Leggi
 e scrivere file MHT
- Supporti
 Mappe XML
- Applicare
 Temi di MS Excel 2007/2010 ai grafici



Altre caratteristiche degne di nota, miglioramenti e correzioni sono riportate di seguito.

 Nuove caratteristiche

 – Supporta le impostazioni per la valutazione della formula di transizione

 Miglioramenti

- Formatta i valori delle celle con le impostazioni locali specificate dall'utente

 Eccezioni

- I file di font non supportati possono causare errori di salvataggio in PDF con eccezioni

 Insetti

- Il metodo Cell.setR1C1Formula() non funzionava correttamente senza offset di colonna
- L'intervallo denominato è stato creato due volte
- Il metodo sortNames() ha causato un'eccezione durante il salvataggio di un file XLSM
- Il numero non è stato formattato correttamente per la frazione
- PDF vuoto generato per PrintOrderType.OVER_POI_FUORI USO
- Il colore di sfondo e le griglie non sono corretti nel PDF generato
- Le funzioni di intercetta e pendenza non sono state calcolate correttamente
- Rimuovi il limite di 33k degli elementi del campo Pivot per i formati di file Excel 2007
- La notazione 1:1 non è supportata nella funzione IF
- La formula DATEDIF è stata calcolata in modo errato
- Ricerca errata delle celle in caso di riga con nome
