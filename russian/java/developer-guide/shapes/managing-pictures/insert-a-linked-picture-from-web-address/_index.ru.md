---
title: Вставить связанное изображение с веб-адреса
type: docs
weight: 50
url: /ru/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Иногда вам нужно вставить изображение из Интернета (http://) на лист. Для этого укажите URL-адрес изображения, и изображение будет загружаться каждый раз при открытии электронной таблицы в Microsoft Excel. Изображение физически не встроено в документ Excel, а указывает на веб-ресурс.

{{% /alert %}}

## **Вставка связанного изображения из веб-адреса**

### **Использование Microsoft Excel**

В Microsoft Excel (например, 2007):

1.  Нажмите на**Вставлять** меню и выберите**Картина**.

![дело:изображение_альтернативный_текст](insert-a-linked-picture-from-web-address_1.png)

1.  Укажите веб-адрес изображения в диалоговом окне «Вставить изображение».

![дело:изображение_альтернативный_текст](insert-a-linked-picture-from-web-address_2.png)

Изображение вставлено.

![дело:изображение_альтернативный_текст](insert-a-linked-picture-from-web-address_3.png)

### **Используя Aspose.Cells for Java**

 Aspose.Cells for Java поддерживает добавление связанного изображения с помощью метода[**ShapeCollection.addLinkedPicture (int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

 Метод возвращает[**Картина**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)объект.

В следующем примере показано, как добавить связанное изображение с веб-адреса на лист.

После запуска кода сгенерированный файл Excel содержит связанное изображение на первом листе.

**Выходной файл** 

![дело:изображение_альтернативный_текст](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
