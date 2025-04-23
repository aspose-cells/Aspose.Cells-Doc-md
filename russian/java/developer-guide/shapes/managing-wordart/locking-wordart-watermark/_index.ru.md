---
title: Блокировка водяного знака WordArt
type: docs
weight: 160
url: /ru/java/locking-wordart-watermark/
---

{{% alert color="primary" %}}

API Aspose.Cells позволяет добавлять водяные знаки WordArt на листе так, чтобы WordArt становился объектом, который можно перемещать и позиционировать на листе. Также возможно заблокировать объект WordArt для любого взаимодействия, такого как редактирование, перемещение и выделение. Эта статья объясняет использование метода [**Shape.setLockedProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#setLockedProperty-int-boolean-) для блокировки нескольких аспектов водяного знака.

{{% /alert %}}

## **Блокировка водяного знака WordArt**

API Aspose.Cells позволяют блокировать определенные аспекты водяного знака, чтобы пользовательское взаимодействие могло быть ограничено или полностью заблокировано. В следующем фрагменте кода демонстрируется использование API Aspose.Cells for Java для создания водяного знака для каждого листа в загруженной электронной таблице и блокировки выбора, перемещения, редактирования и изменения размера водяного знака.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LockWordArtWatermark-LockWordArtWatermark.java" >}}
{{< app/cells/assistant language="java" >}}
