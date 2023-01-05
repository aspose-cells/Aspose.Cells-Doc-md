---
title: Satırları ve Sütunları Yeniden Boyutlandırma
type: docs
weight: 30
url: /tr/net/resize-rows-and-columns/
---
{{% alert color="primary" %}} 

Bazen hücre değerleri, içinde bulundukları hücreden daha geniştir veya birkaç satırdadır. Bu tür değerler, satırların ve sütunların yükseklik ve genişliklerini değiştirmedikçe kullanıcılar tarafından tam olarak görülemez. Aspose.Cells.GridWeb, satır yüksekliklerini ve sütun genişliğini ayarlamayı tamamen destekler. Bu konuda, bu özellikler örnekler yardımıyla ayrıntılı olarak ele alınmaktadır.

{{% /alert %}} 
## **Satır Yükseklikleri ve Sütun Genişliği ile Çalışma**
### **Satır Yüksekliğini Ayarlama**
Bir satırın yüksekliğini ayarlamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Çalışma sayfasının Cells koleksiyonuna erişin.
1. Belirtilen herhangi bir satırdaki tüm hücrelerin yüksekliğini ayarlayın.

{{% alert color="primary" %}} 

Cells koleksiyonunun SetRowHeight ve SetColumnWidth yönteminde satır yüksekliği ve sütun genişliği ölçümlerini inç ve piksel olarak ayarlamak için kullanılabilen değişkenler de vardır.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetRowHeight.cs" >}}
### **Sütun Genişliğini Ayarlama**
Bir sütunun genişliğini ayarlamak için:

1. Aspose.Cells.GridWeb denetimini Web Formunuza ekleyin.
1. Çalışma sayfasının Cells koleksiyonuna erişin.
1. Belirtilen herhangi bir sütundaki tüm hücrelerin genişliğini ayarlayın.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-ResizeRowsColumns.aspx-SetColumnWidth.cs" >}}
