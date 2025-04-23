---
title: Uppdatera ActiveX ComboBox kontroll
type: docs
weight: 170
url: /sv/python-net/update-activex-combobox-control/
---

## **Möjliga användningsscenario**
Du kan läsa eller skriva värdena för ActiveX ComboBox-kontrollen med Aspose.Cells för Python via .NET. Vänligen nå ActiveX-kontrollen via [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) egenskapen och kontrollera dess typ via [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/) egenskapen, den bör returnera [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype)-värde och då kasta om det till [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) objekt och läs eller ändra dess olika egenskaper.

Vänligen ladda ner den [provexemplet Excel-fil](5115124.xlsx) som används i följande provkod.
## **Uppdatera ActiveX ComboBox Control**
Följande skärmbild visar effekten av provkoden på den [provexemplet Excel-filen](5115124.xlsx). Som du kan se har ActiveX ComboBox-värdet uppdaterats till "Detta är kombinationsruta-kontroll".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Exempelkod**
Följande provkod uppdaterar värdet för ActiveX ComboBox Control som finns i [provexemplet Excel-filen](5115124.xlsx).



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
