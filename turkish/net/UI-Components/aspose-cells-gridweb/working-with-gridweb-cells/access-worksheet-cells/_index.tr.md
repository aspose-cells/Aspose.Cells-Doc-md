---
title: Erişim Çalışma Sayfası Cells
type: docs
weight: 10
url: /tr/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

Bu konuda, Aspose.Cells.GridWeb'in en temel özelliği olan hücrelere erişim incelenerek hücreler ele alınmaktadır.

{{% /alert %}} 
## **Bir Çalışma Sayfasında Cells'e Erişme**
Her çalışma sayfası, aslında GridCell nesnelerinin bir koleksiyonu olan Cells adında bir özellik içerir; burada bir GridCell nesnesi, Aspose.Cells.GridWeb'de bir hücreyi temsil eder. Aspose.Cells.GridWeb kullanarak herhangi bir hücreye erişmek mümkündür. Her biri aşağıda tartışılan tercih edilen iki yöntem vardır.


### **Cell Adını Kullanma**
Tüm hücrelerin benzersiz bir adı vardır. Örneğin, A1, A2, B1, B2 vb. Aspose.Cells.GridWeb, geliştiricilerin hücre adını kullanarak istenen herhangi bir hücreye erişmesine olanak tanır. Hücre adını (bir dizin olarak) GridWorksheet'in Cells koleksiyonuna geçirmeniz yeterlidir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **Satır ve Sütun İndekslerini Kullanma**
Bir hücre, satır ve sütun indeksleri cinsinden konumuna göre de tanınabilir. Bir hücrenin satır ve sütun dizinlerini GridWorksheet'in Cells koleksiyonuna geçirmeniz yeterlidir. Bu yaklaşım yukarıdakinden daha hızlıdır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
