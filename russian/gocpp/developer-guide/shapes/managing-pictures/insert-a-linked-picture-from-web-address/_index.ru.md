---
title: Вставить связанное изображение с веб адреса с помощью Golang через C++
linktitle: Вставить связанное изображение из веб адреса
type: docs
weight: 450
url: /ru/go-cpp/insert-a-linked-picture-from-web-address/
description: Узнайте, как вставлять связанную картинку из веб адреса в лист с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Иногда вам может потребоваться вставить изображение из интернета (http://) в таблицу. Для этого укажите URL изображения, и изображение будет загружаться каждый раз при открытии электронной таблицы в Microsoft Excel. Изображение фактически не вставляется в документ Excel, а указывает на веб-ресурс.

{{% /alert %}}

## **Использование Microsoft Excel**

В Microsoft Excel (например, 2007 год):

1. Нажмите меню **Вставка** и выберите **Изображение**.
1. Укажите веб-адрес изображения в диалоговом окне Вставки изображения.

## **Использование Aspose.Cells for C++**

Aspose.Cells for C++ поддерживает добавление связанного изображения с помощью метода [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/). Этот метод возвращает объект [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/). 

Следующий пример показывает, как добавить связанное изображение из веб-адреса в лист.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
