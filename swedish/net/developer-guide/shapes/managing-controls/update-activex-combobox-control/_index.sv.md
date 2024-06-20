---
title: Uppdatera ActiveX ComboBox kontroll
type: docs
weight: 170
url: /sv/net/update-activex-combobox-control/
---

## **Möjliga användningsscenario**
Du kan läsa eller skriva värdena för ActiveX ComboBox Control med hjälp av Aspose.Cells. Vänligen kom åt ActiveX Control via [Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol)-egenskapen och kontrollera dess typ via [ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type)-egenskapen, den bör returnera värdet [ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) och sedan typkonvertera den till [ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol)-objekt och läsa eller ändra dess olika egenskaper.

Vänligen ladda ner den [provexemplet Excel-fil](5115124.xlsx) som används i följande provkod.
## **Uppdatera ActiveX ComboBox Control**
Följande skärmbild visar effekten av provkoden på den [provexemplet Excel-filen](5115124.xlsx). Som du kan se har ActiveX ComboBox-värdet uppdaterats till "Detta är kombinationsruta-kontroll".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Exempelkod**
Följande provkod uppdaterar värdet för ActiveX ComboBox Control som finns i [provexemplet Excel-filen](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
