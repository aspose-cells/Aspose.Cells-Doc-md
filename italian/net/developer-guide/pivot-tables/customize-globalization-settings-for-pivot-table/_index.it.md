---
title: Personalizza le impostazioni di globalizzazione per la tabella pivot
type: docs
weight: 50
url: /it/net/customize-globalization-settings-for-pivot-table/
---
##  **Possibili scenari di utilizzo**

 A volte vuoi personalizzare il*Totale pivot, Totale parziale, Totale generale, Tutti gli elementi, Elementi multipli, Etichette di colonna, Etichette di riga, Valori vuoti*testo secondo le vostre esigenze. Aspose.Cells consente di personalizzare le impostazioni di globalizzazione della tabella pivot per gestire tali scenari. Puoi anche utilizzare questa funzione per modificare le etichette in altre lingue come arabo, hindi, polacco, ecc.

##  **Personalizza le impostazioni di globalizzazione per la tabella pivot**

Il seguente codice di esempio spiega come personalizzare le impostazioni di globalizzazione per la tabella pivot. Crea una classe*Impostazioni di globalizzazione della tabella pivot personalizzata* derivato da una classe base[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)e sovrascrive tutti i suoi metodi necessari. Questi metodi restituiscono il testo personalizzato per *Totale pivot, Subtotale, Totale generale, Tutti gli elementi, Elementi multipli, Etichette di colonna, Etichette di riga, Valori vuoti*. Quindi assegna l'oggetto di questa classe a[**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/) proprietà. Il codice carica il file[file Excel di origine](40468488.xlsx) che contiene la tabella pivot, aggiorna e calcola i suoi dati e li salva come[uscita PDF](40468487.pdf) file. Lo screenshot seguente mostra l'effetto del codice di esempio sull'output PDF. Come puoi vedere nello screenshot, diverse parti della tabella pivot ora hanno un testo personalizzato restituito dai metodi sovrascritti di[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)classe.

![cose da fare:immagine_alt_testo](customize-globalization-settings-for-pivot-table_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
