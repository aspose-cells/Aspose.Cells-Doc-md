---
title: Aspose.Cells for Java 2.5.2 Note di rilascio
type: docs
weight: 70
url: /it/java/aspose-cells-for-java-2-5-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 2.5.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-2.5.2/)

{{% /alert %}} 

 Siamo felici di annunciare Aspose.Cells for Java 2.5.2!

 Cosa è cambiato:

- Supporta la lettura delle tabelle pivot dai file modello.
 Aggiunge LineShape ai file Excel 2007 XLSX.
 Fornisce supporto per impostare il nome della serie durante l'impostazione dell'origine dati del grafico.
 Supporta per ottenere/impostare la visibilità delle linee della griglia di diversi fogli di lavoro nei file ODS.
 È stato apportato un miglioramento per la lettura delle forme dai file XLSX.
 Sono stati apportati miglioramenti alle funzionalità da grafico a immagine, da foglio a immagine e da Excel a PDF.
 È stato apportato un miglioramento per l'analisi delle formule.
 Il miglioramento è fatto per la copia Cells.
31 correzioni e miglioramenti.

 Problemi risolti in Aspose.Cells for Java 2.5.2.





 Cambiamenti notevoli per gli utenti:



 Nelle vecchie versioni, FormatCondition.getStyle() faceva in modo che FormatConditions mantenesse il proprio oggetto Style. La modifica dell'oggetto Style restituito di getStyle() successivamente modificherebbe direttamente lo stile di FormatCondition.

Da questa versione, FormatCondition utilizzerà una classe di stile più concreta DXFStyle (una sottoclasse di Style, con la quale possiamo fornire funzionalità più flessibili da supportare in futuro). Ad esempio, ora FormatCondition.getStyle() restituirà una copia dell'oggetto DXFStyle invece dell'oggetto Style. E consigliamo agli utenti di utilizzare l'oggetto DXFStyle per il metodo FormatCondition.setStye(Style). Tutti gli oggetti Style impostati su FormatCondition verranno convertiti in DXFStyle e raccolti in un pool globale per la cartella di lavoro. Pertanto FormatCondition manterrà solo un riferimento DXFStyle. La successiva modifica dell'oggetto DXFStyle restituito di getStyle() non cambierà lo stile di FormatCondition. Per rendere effettiva la modifica, gli utenti devono chiamare setStyle() per FormatCondition dopo che lo stile è stato modificato.
