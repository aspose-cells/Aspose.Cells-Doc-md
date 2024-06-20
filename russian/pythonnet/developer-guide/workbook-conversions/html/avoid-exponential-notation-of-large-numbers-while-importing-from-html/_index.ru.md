---
title: Избегайте экспоненциальной нотации больших чисел при импорте из HTML
type: docs
weight: 10
url: /ru/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Эта тема показывает, как избежать экспоненциальной нотации больших чисел при импорте из HTML с использованием Aspose.Cells для Python via NET.
keywords: Избегайте экспоненциальной нотации больших чисел при импорте из HTML, сохраняйте точность при импорте HTML.
---

{{% alert color="primary" %}}

Иногда в вашем HTML содержатся числа, например, 1234567890123456, которые длиннее 15 цифр, и при импорте вашего HTML в файл Excel эти числа преобразуются в экспоненциальную запись, например, 1.23457Е+15. Если вы хотите, чтобы ваше число импортировалось как есть и не преобразовывалось в экспоненциальную запись, то пожалуйста, используйте свойство [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) и установите его в **true** при загрузке вашего HTML.

{{% /alert %}}

В следующем образце кода объясняется использование свойства [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/). API импортирует число как есть, не преобразуя его в экспоненциальную нотацию.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
