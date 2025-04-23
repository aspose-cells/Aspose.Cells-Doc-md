---
title: Personalizza le impostazioni di globalizzazione per la tabella pivot
type: docs
weight: 50
url: /it/net/customize-globalization-settings-for-pivot-table/
---

## **Possibili Scenari di Utilizzo**

A volte si desidera personalizzare i testi *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* in base alle proprie esigenze. Aspose.Cells consente di personalizzare le impostazioni di globalizzazione della tabella pivot per gestire tali scenari. È inoltre possibile utilizzare questa funzionalità per modificare le etichette in altre lingue come arabo, hindi, polacco, ecc.

## **Personalizza le impostazioni di globalizzazione per la tabella pivot**

Il seguente codice di esempio spiega come personalizzare le impostazioni di globalizzazione per la tabella pivot. Crea una classe *CustomPivotTableGlobalizationSettings* derivata da una classe di base [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/) e ne sovrascrive tutti i metodi necessari. Questi metodi restituiscono il testo personalizzato per i *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*. Quindi assegna l'oggetto di questa classe alla proprietà [**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/). Il codice carica il [file excel di origine](40468488.xlsx) che contiene la tabella pivot, aggiorna e calcola i dati e lo salva come file [PDF di output](40468487.pdf). La seguente schermata mostra l'effetto del codice di esempio sul PDF di output. Come si può vedere nella schermata, diverse parti della tabella pivot hanno ora un testo personalizzato restituito dai metodi sovrascritti della classe [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/).

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
