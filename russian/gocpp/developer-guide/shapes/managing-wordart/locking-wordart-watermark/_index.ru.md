---
title: Блокировка водяного знака WordArt с помощью Golang через C++
linktitle: Блокировка водяного знака WordArt
type: docs
weight: 170
url: /ru/go-cpp/locking-wordart-watermark/
description: Узнайте, как блокировать водяные знаки WordArt в Excel с помощью Aspose.Cells for C++. Предотвращайте редактирование, перемещение и выбор водяных знаков программно.
---

{{% alert color="primary" %}}

APIs Aspose.Cells позволяют добавлять водяные знаки WordArt на лист так, что WordArt становится объектом, который можно перемещать и размещать на листе. Также возможно заблокировать объект WordArt для взаимодействий, таких как редактирование, перемещение и выбор. В этой статье объясняется использование метода [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/go-cpp/shape/setlockedproperty/) для блокировки некоторых аспектов водяного знака.

{{% /alert %}}

APIs Aspose.Cells позволяют блокировать определённые аспекты водяного знака, чтобы ограничить или полностью заблокировать взаимодействие пользователя. Следующий фрагмент кода демонстрирует использование API Aspose.Cells for C++ для блокировки выделения, перемещения, редактирования и изменения размера водяного знака, создавая таблицу с нуля.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LockingWordartWatermark.go" >}}
