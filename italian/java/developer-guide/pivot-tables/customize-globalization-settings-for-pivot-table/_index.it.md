---
title: Personalizza le impostazioni di globalizzazione per la tabella pivot
type: docs
weight: 20
url: /it/java/customize-globalization-settings-for-pivot-table/
---
## **Possibili scenari di utilizzo**

 A volte vuoi personalizzare il file*Totale pivot, totale parziale, totale complessivo, tutti gli elementi, più elementi, etichette di colonna, etichette di riga, valori vuoti*testo secondo le vostre esigenze. Aspose.Cells consente di personalizzare le impostazioni di globalizzazione della tabella pivot per affrontare tali scenari. Puoi anche utilizzare questa funzione per cambiare le etichette in altre lingue come arabo, hindi, polacco, ecc.

## **Personalizza le impostazioni di globalizzazione per la tabella pivot**

 Il seguente codice di esempio spiega come personalizzare le impostazioni di globalizzazione per la tabella pivot. Crea una classe*Impostazioni di globalizzazione della tabella pivot personalizzata* derivato da una classe base[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) e sovrascrive tutti i suoi metodi necessari. Questi metodi restituiscono il testo personalizzato per il file*Totale pivot, totale parziale, totale complessivo, tutti gli elementi, più elementi, etichette di colonna, etichette di riga, valori vuoti* . Quindi assegna l'oggetto di questa classe a[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) proprietà. Il codice carica il file[file excel di origine](40468491.xlsx) che contiene la tabella pivot, aggiorna e calcola i suoi dati e li salva come[file di output PDF](40468490.pdf) . Lo screenshot seguente mostra l'effetto del codice di esempio sul PDF di output. Come puoi vedere nello screenshot, diverse parti della tabella pivot hanno ora un testo personalizzato restituito dai metodi sovrascritti di[**Impostazioni di globalizzazione**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)classe.

![cose da fare:immagine_alt_testo](customize-globalization-settings-for-pivot-table_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
