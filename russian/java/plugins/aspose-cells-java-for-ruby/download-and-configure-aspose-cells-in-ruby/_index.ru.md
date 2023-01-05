---
title: Загрузите и настройте Aspose.Cells в Ruby
type: docs
weight: 10
url: /ru/java/download-and-configure-aspose-cells-in-ruby/
---
## **Скачать необходимые библиотеки**
Загрузите необходимые библиотеки, указанные ниже. Они необходимы для выполнения Aspose.Cells Java для примеров Ruby.

- [Aspose.Cell for Java Компонент](https://downloads.aspose.com/cells/java/)
## **Загрузите примеры с сайтов социального кодирования**
Следующие выпуски работающих примеров доступны для загрузки на указанных ниже сайтах социального кодирования:

**Гитхаб**

- [Aspose.Cells Java для рубина](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Установка**
Это очень просто и легко установить Aspose.cells Java для Ruby gem, выполните следующие простые шаги:

1.  Добавьте эту строку в Gemfile вашего приложения.

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. А затем выполнить

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**ИЛИ ЖЕ**

1.  Запустите следующую команду.

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **С использованием**
Включите необходимые файлы для работы с примером helloworld.

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Давайте разберемся с приведенным выше кодом.

1. Первая строка обеспечивает загрузку и доступность ячеек aspose.
1. Включите файлы, необходимые для доступа к ячейкам aspose.
1. Инициализируйте библиотеки. Классы aspose JAVA загружаются из пути, указанного в файле aspose.yml/
