---
title: Вставить связанное изображение с веб-адреса
type: docs
weight: 450
url: /ru/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Иногда вам нужно вставить изображение из Интернета (http://) на лист. Для этого укажите URL-адрес изображения, и изображение будет загружаться каждый раз при открытии электронной таблицы в Microsoft Excel. Изображение физически не встроено в документ Excel, а указывает на веб-ресурс.

{{% /alert %}}

## **Использование Microsoft Excel**

В Microsoft Excel (например, 2007):

1.  Нажмите на**Вставлять** меню и выберите**Рисунок**.
1. Укажите веб-адрес изображения в диалоговом окне «Вставить изображение».

## **Используя Aspose.Cells for .NET**

 Aspose.Cells for .NET поддерживает добавление связанного изображения с помощью[**ShapeCollection.AddLinkedPicture (int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) . Метод возвращает[**Рисунок**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)объект.

В следующем примере показано, как добавить связанное изображение с веб-адреса на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
