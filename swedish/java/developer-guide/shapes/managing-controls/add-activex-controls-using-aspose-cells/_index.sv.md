---
title: Lägg till ActiveX kontroller med hjälp av Aspose.Cells
type: docs
weight: 720
url: /sv/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Du kan lägga till ActiveX-kontroller med Aspose.Cells med hjälp av [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) metoden. Denna metod tar en parameter [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) som talar om vilken typ av ActiveX-kontroll som ska läggas till i en arbetsbok. Den har följande värden.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [TEXT_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [TOGGLE_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [OKÄND](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

När du har lagt till ActiveX-kontrollen i formkollektionen kan du sedan komma åt ActiveX-kontrollobjektet via egenskapen [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) och sedan ställa in dess olika egenskaper.

{{% /alert %}} 
## **Lägg till knappen Aktivera knappen via Aspose.Cells**
Nedanstående exempelkod lägger till aktiveringsknappen Aktivera knappen via Aspose.Cells. Vänligen ladda ner den [utdataexcel-fil](5473427.xlsx) som genereras med denna kod för din referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
