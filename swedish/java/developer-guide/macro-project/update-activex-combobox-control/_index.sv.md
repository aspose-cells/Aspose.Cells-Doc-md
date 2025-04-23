---
title: Uppdatera ActiveX ComboBox kontroll
type: docs
weight: 900
url: /sv/java/update-activex-combobox-control/
---

## **Möjliga användningsscenario**
Du kan läsa eller skriva värdena för ActiveX ComboBox Kontroll med Aspose.Cells. Ha tillgång till ActiveX-kontrollen via egenskapen [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) och kontrollera dess typ med egenskapen [ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type), den bör returnera värdet [ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX) och sedan kan du typomvandla den till objektet [ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) och läsa eller ändra dess olika egenskaper.

Vänligen ladda ner den [prov Excel-fil](5473374.xlsx) som används i den följande exempelkoden och [utdata Excel-filen](5473375.xlsx) genererad av den.
## **Uppdatera ActiveX ComboBox Control**
Följande skärmbild visar effekten av exempelkoden på den [prov Excel-fil](5473374.xlsx). Som du kan se har värdet för ActiveX ComboBox uppdaterats till "Detta är kombo box-kontroll".

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **Exempelkod**
Följande exempelkod uppdaterar värdet på ActiveX ComboBox Control som finns inne i [prov Excel-fil](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
{{< app/cells/assistant language="java" >}}
