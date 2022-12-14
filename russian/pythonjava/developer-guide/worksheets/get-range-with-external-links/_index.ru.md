---
title: Получить диапазон с внешними ссылками
type: docs
weight: 60
url: /ru/python-java/get-range-with-external-links/
---
## **Получить диапазон с внешними ссылками**
Во многих случаях файлы Excel получают доступ к данным из других файлов Excel с помощью внешних ссылок. Aspose.Cells для Python через Java предоставляет возможность получить эти внешние ссылки с помощью[Имя.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) метод.[Имя.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) возвращает массив типа[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea).[ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)класс предоставляет[ИмяВнешнегоФайла](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName)свойство, которое возвращает имя внешнего файла.

Следующий фрагмент кода показывает, как получить внешние ссылки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
