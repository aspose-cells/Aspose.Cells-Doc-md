---
title: Получить диапазон с внешними ссылками
type: docs
weight: 60
url: /ru/python-java/get-range-with-external-links/
---

## **Получить диапазон с внешними ссылками**
Существует множество случаев, когда файлы Excel получают доступ к данным других файлов Excel с помощью внешних ссылок. Aspose.Cells для Python via Java предоставляет возможность получать эти внешние ссылки с помощью метода [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)). Метод [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) возвращает массив типа [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). Класс [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) предоставляет свойство [ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName), которое возвращает имя внешнего файла.

В следующем фрагменте кода показано, как получить внешние ссылки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
