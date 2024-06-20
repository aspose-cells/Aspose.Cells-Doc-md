---
title: Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulayın
type: docs
weight: 90
url: /tr/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların çalışma sayfası hücrelerine veri doğrulama kuralları eklemesine izin verir. Örneğin, on ve yirmi arasındaki sayıları sınırlamak için ondalık doğrulama uygulanabilir. Bu belirtilen aralığın dışında başka bir sayı girilirse, Microsoft Excel bir hata mesajı gösterir ve kullanıcıyı doğru aralıktan bir sayıyı yeniden girmeye zorlar. Kullanıcı sayı yapıştırdığında, örneğin 3, hücreye, Excel doğrulama kontrolünü çalıştırmaz veya hata mesajı göstermez.

{{% /alert %}}

## Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulayın

Bazen, bir verilen değerin, hücreye uygulanan veri doğrulama kurallarına uyup uymadığını dinamik olarak doğrulamak gereklidir. Bu amaçla, Aspose.Cells API'leri [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) yöntemini sağlar. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa **False** döndürür, aksi takdirde **True** döndürür.

Aşağıdaki örnek Microsoft Excel dosyası, aşağıdaki örnek kodla test etmek için kullanılır: C1 hücresinin **ondalık veri doğrulama** uygulandığını ve yalnızca **10 ile 20 arasındaki değerleri** kabul edeceğini görebilirsiniz. Hücre değeri 10 ile 20 arasında olduğunda, [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) yöntemi **True** döndürecektir, aksi halde **False** döndürecektir.

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

Aşağıdaki örnek kod, [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) yönteminin nasıl çalıştığını gösterir. İlk olarak, C1'e değer 3 girer. Bu, veri doğrulama kuralını karşılamadığı için, [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) yöntemi **False** döndürür. Sonra, C1'e değer 15 girer. Bu değer, veri doğrulama kuralını karşıladığı için, [**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--) yöntemi **True** döndürür. Benzer şekilde, 30 değeri için **False** döndürür.

## Bir Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulamak için Java Kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Örnek Kod Tarafından Oluşturulan Konsol Çıktısı

Aşağıdaki örnek Excel dosyasıyla çalıştırıldığında oluşturulan konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
