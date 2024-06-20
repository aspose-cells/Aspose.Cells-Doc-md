---
title: Вставить связанное изображение из веб адреса
type: docs
weight: 50
url: /ru/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться вставить изображение из интернета (http://) в таблицу. Для этого укажите URL изображения, и изображение будет загружаться каждый раз при открытии электронной таблицы в Microsoft Excel. Изображение фактически не вставляется в документ Excel, а указывает на веб-ресурс.

{{% /alert %}}

## **Вставка связанного изображения из веб-адреса**

### **Использование Microsoft Excel**

В Microsoft Excel (например, 2007 год):

1. Нажмите меню **Вставка** и выберите **Изображение**.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. Укажите веб-адрес изображения в диалоговом окне Вставки изображения. 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

Изображение вставлено.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **Используя Aspose.Cells for Java**

Aspose.Cells for Java поддерживает добавление связанного изображения с использованием метода [**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

Метод возвращает объект [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

В следующем примере показано, как добавить связанное изображение из веб-адреса в таблицу.

После выполнения кода сгенерированный файл Excel содержит связанное изображение на первом листе.

**Выходной файл** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
