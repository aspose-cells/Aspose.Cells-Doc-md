---
title: Personalizza le impostazioni di globalizzazione per la tabella pivot
type: docs
weight: 20
url: /it/java/customize-globalization-settings-for-pivot-table/
---

## **Possibili Scenari di Utilizzo**

A volte si desidera personalizzare i testi *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* in base alle proprie esigenze. Aspose.Cells consente di personalizzare le impostazioni di globalizzazione della tabella pivot per gestire tali scenari. È inoltre possibile utilizzare questa funzionalità per modificare le etichette in altre lingue come arabo, hindi, polacco, ecc.

## **Personalizza le impostazioni di globalizzazione per la tabella pivot**

Il seguente esempio di codice spiega come personalizzare le impostazioni di globalizzazione per la tabella pivot. Crea una classe *CustomPivotTableGlobalizationSettings* derivata da una classe di base [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) e ne sovrascrive tutti i metodi necessari. Questi metodi restituiscono il testo personalizzato per *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*. Quindi assegna l'oggetto di questa classe a una proprietà [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings). Il codice carica il [file Excel di origine](40468491.xlsx) che contiene la tabella pivot, aggiorna e calcola i dati e li salva come [file PDF di output](40468490.pdf). La seguente schermata mostra l'effetto del codice di esempio sul file PDF di output. Come si può vedere nella schermata, diverse parti della tabella pivot hanno ora un testo personalizzato restituito dai metodi sovrascritti della classe [**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
{{< app/cells/assistant language="java" >}}
