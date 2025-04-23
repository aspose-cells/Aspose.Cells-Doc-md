---
title: Вставить связанное изображение из веб адреса
type: docs
weight: 450
url: /ru/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться вставить изображение из интернета (http://) в таблицу. Для этого укажите URL изображения, и изображение будет загружаться каждый раз при открытии электронной таблицы в Microsoft Excel. Изображение фактически не вставляется в документ Excel, а указывает на веб-ресурс.

{{% /alert %}}

## **Использование Microsoft Excel**

В Microsoft Excel (например, 2007 год):

1. Нажмите меню **Вставка** и выберите **Изображение**.
1. Укажите веб-адрес изображения в диалоговом окне Вставки изображения.

## **Использование Aspose.Cells for Python via .NET**

Aspose.Cells для Python via .NET поддерживает добавление связанного изображения с помощью метода [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture). Этот метод возвращает объект [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

В следующем примере показано, как добавить связанное изображение из веб-адреса в таблицу.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
