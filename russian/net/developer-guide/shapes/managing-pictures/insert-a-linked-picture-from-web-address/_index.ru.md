---
title: Вставить связанное изображение из веб адреса
type: docs
weight: 450
url: /ru/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться вставить изображение из интернета (http://) в таблицу. Для этого укажите URL изображения, и изображение будет загружаться каждый раз при открытии электронной таблицы в Microsoft Excel. Изображение фактически не вставляется в документ Excel, а указывает на веб-ресурс.

{{% /alert %}}

## **Использование Microsoft Excel**

В Microsoft Excel (например, 2007 год):

1. Нажмите меню **Вставка** и выберите **Изображение**.
1. Укажите веб-адрес изображения в диалоговом окне Вставки изображения.

## **Использование Aspose.Cells for .NET**

Aspose.Cells for .NET поддерживает добавление связанного изображения с использованием [**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture). Метод возвращает объект [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

В следующем примере показано, как добавить связанное изображение из веб-адреса в таблицу.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
