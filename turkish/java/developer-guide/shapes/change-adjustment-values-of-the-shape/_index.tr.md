---
title: Şekil Ayar Değerlerini Değiştir
type: docs
weight: 3200
url: /tr/java/change-adjustment-values-of-the-shape/
---

{{% alert color="primary" %}} 

Aspose.Cells, şekillerle ilgili ayar noktalarını değiştirmek için [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) özelliğini sağlar. Microsoft Excel kullanıcı arayüzünde ayarlar, sarı elmas düğümleri olarak görüntülenir. Örneğin:

- Yuvarlatılmış Dikdörtgenin yay değiştirmek için ayarlaması vardır
- Üçgenin nokta konumunu değiştirmek için bir ayarlaması vardır
- Bir yamuktur, üstünün genişliğini değiştirmek için bir ayarlamaya sahiptir
- Oklar, baş ve kuyruk şeklini değiştirmek için iki ayarlamaya sahiptir

Bu makale, farklı şekillerin ayar değerini değiştirmek için [Shape.getGeometry().getShapeAdjustValues()](https://reference.aspose.com/cells/java/com.aspose.cells/geometry#ShapeAdjustValues) özelliğinin kullanımını açıklayacaktır.

{{% /alert %}} 
## **Şekil Ayar Değerlerini Değiştirme**
Aşağıdaki örnek kod, kaynak excel dosyasındaki ilk üç şekle erişir ve ardından şekillerin ayar değerlerini değiştirir. Aşağıdaki ekran görüntüleri, ayar değerlerini değiştirmeden önce şekillerin nasıl göründüğünü ve ardından ayar değerlerini değiştirdikten sonraki görünümünü göstermektedir.
### **Ayar Değerleri Değiştirilmeden Önce Çizim Şekilleri**
![todo:image_alt_text](change-adjustment-values-of-the-shape_1.png)
### **Ayar Değerleri Değiştirildikten Sonra Çizim Şekilleri**
![todo:image_alt_text](change-adjustment-values-of-the-shape_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAdjustmentValuesOfShape-ChangeAdjustmentValuesOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
