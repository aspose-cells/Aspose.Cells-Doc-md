---
title: Добавьте элементы управления ActiveX, используя Aspose.Cells.
type: docs
weight: 720
url: /ru/java/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}} 

 Вы можете добавить элементы управления ActiveX с номером Aspose.Cells, используя команду[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\) ) метод. Этот метод принимает параметр[тип управления](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)который сообщает, какой тип элемента управления ActiveX необходимо добавить на рабочий лист. Он имеет следующие значения.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [ПОЛЕ СО СПИСКОМ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [ИЗОБРАЖЕНИЕ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [ЭТИКЕТКА](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [ПЕРЕКЛЮЧАТЕЛЬ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [ПОЛОСА ПРОКРУТКИ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [ТЕКСТОВОЕ ОКНО](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [КНОПКА-ПЕРЕКЛЮЧАТЕЛЬ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [НЕИЗВЕСТНЫЙ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

 После того, как вы добавили элемент управления ActiveX в коллекцию фигур, вы можете получить доступ к объекту элемента управления ActiveX через[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) свойство, а затем установить его различные свойства.

{{% /alert %}} 
## **Добавьте элемент управления ActiveX кнопки переключения, используя Aspose.Cells**
 В следующем примере кода добавляется элемент управления ActiveX Toggle Button с использованием Aspose.Cells. Пожалуйста, загрузите[выходной файл excel](5473427.xlsx) сгенерированный с помощью этого кода для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
