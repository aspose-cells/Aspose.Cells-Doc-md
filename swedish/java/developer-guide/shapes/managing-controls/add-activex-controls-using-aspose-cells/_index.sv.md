---
title: Lägg till ActiveX-kontroller med Aspose.Cells
type: docs
weight: 720
url: /sv/java/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}} 

 Du kan lägga till ActiveX-kontroller med Aspose.Cells med hjälp av[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\) ) metod. Denna metod tar en parameter[ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)som talar om vilken typ av ActiveX-kontroll som måste läggas till i ett kalkylblad. Den har följande värden.

- [KRYSSRUTA](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [KOMBINATIONSRUTAN](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [KOMMANDOKNAPP](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [BILD](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [MÄRKA](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO KNAPP](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [RULLNINGSLIST](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [TEXTRUTA](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [VÄXLINGSKNAPP](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [OKÄND](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

 När du väl har lagt till ActiveX-kontrollen i formsamlingen kan du komma åt ActiveX-kontrollobjektet via[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) egenskap och ställ sedan in dess olika egenskaper.

{{% /alert %}} 
## **Lägg till ActiveX-kontroll för växlingsknapp med Aspose.Cells**
 Följande exempelkod lägger till ActiveX-kontroll för Toggle Button med Aspose.Cells. Ladda ner[output excel-fil](5473427.xlsx) genereras med den här koden för din referens.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
