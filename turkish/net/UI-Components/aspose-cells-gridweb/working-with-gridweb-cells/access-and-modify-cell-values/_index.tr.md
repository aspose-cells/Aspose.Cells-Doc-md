---
title: Hücre Değerine Erişme ve Değiştirme
type: docs
weight: 20
url: /tr/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb, hücre değeri, değiştirme, değer
description: Bu makale, GridWeb de hücre değerine nasıl erişilip değiştirileceğini tanıtır.
---

{{% alert color="primary" %}} 

[Hücrelere Erişme](/cells/tr/net/aspose-cells-gridweb/access-worksheet-cells/) hücrelere erişmeyi tartışmıştı. Bu konu, Aspose.Cells.GridWeb API'sını kullanarak hücre değerlerine nasıl erişileceğini göstermek için o tartışmayı genişletir.

{{% /alert %}} 
## **Hücrenin Değerine Erişme ve Değiştirme**
### **Dize Değerleri**
Bir hücrenin değerine erişmeden ve bunu değiştirmeden önce, hücrelere erişmenin farklı yaklaşımları hakkında bilgi sahibi olmanız gerekir. Hücrelere erişimin farklı yaklaşımları hakkında ayrıntılı bilgi için [Hücrelere Erişme](/cells/tr/net/aspose-cells-gridweb/access-worksheet-cells/) buraya bakın.

Her hücrenin StringValue adında bir özelliği vardır. Bir hücreye erişildikten sonra, geliştiriciler StringValue özelliğini hücrenin dize değerine erişmek için kullanabilirler. Hücre değerlerini değiştirmek için, hücrenin dize değerini güncellemek için kullanılan PutValue adlı özel bir yöntem bulunmaktadır.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **Tüm Değer Türleri**
Bir hücrenin PutValue yönteminin kullanılabilmesi için 8 aşırı yüklemesi bulunmaktadır, bu aşırı yüklemeler hücrede herhangi bir türde değeri (Boolean, int, double, DateTime ve dize) değiştirmek için kullanılabilir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



Ayrıca PutValue yönteminin dize biçiminde herhangi bir türde değeri alabilen aşırı yüklenmiş bir sürümü de bulunmaktadır ve bunu yapabilmek için, aşağıdaki örnekte gösterildiği gibi, PutValue yönteminin başka bir parametresine true Boolean değeri geçirin.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
