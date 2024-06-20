---
title: Добавление элементов ActiveX с помощью Aspose.Cells
type: docs
weight: 720
url: /ru/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Вы можете добавлять элементы ActiveX с помощью Aspose.Cells, используя метод [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\)). Этот метод принимает параметр [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType), который указывает, какой тип элемента ActiveX нужно добавить в рабочий лист. У него есть следующие значения.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [КНОПКА ВРАЩЕНИЯ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [ТЕКСТОВОЕ ПОЛЕ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [КНОПКА ПЕРЕКЛЮЧЕНИЯ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [НЕИЗВЕСТНО](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

После того как вы добавите элемент ActiveX в коллекцию форм, вы сможете получить доступ к объекту элемента ActiveX через свойство [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl), а затем установить его различные свойства.

{{% /alert %}} 
## **Добавить элемент управления переключения ActiveX используя Aspose.Cells**
Следующий образец кода добавляет элемент управления переключения ActiveX с помощью Aspose.Cells. Пожалуйста, загрузите [файл Excel](5473427.xlsx), сгенерированный с помощью этого кода, для вашего справочного пособия.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
