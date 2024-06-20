---
title: Скачайте и настройте Aspose.Cells в Ruby
type: docs
weight: 10
url: /ru/java/download-and-configure-aspose-cells-in-ruby/
---

## **Загрузить необходимые библиотеки**
Загрузите необходимые библиотеки, упомянутые ниже. Они необходимы для выполнения примеров Aspose.Cells Java для Ruby.

- [Компонент Aspose.Cell для Java](https://downloads.aspose.com/cells/java/)
## **Загрузить примеры из сайтов социального кодирования**
Следующие версии выполняемых примеров доступны для загрузки на указанных ниже сайтах социального кодирования:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Установка**
Установка Aspose.cells Java для Ruby gem очень проста и легка, пожалуйста, следуйте этим простым шагам:

1. Добавьте эту строку в файл Gemfile вашего приложения. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. Затем выполните команду 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**ИЛИ**

1. Выполните следующую команду. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **Использование**
Включите необходимые файлы для работы с примером helloworld.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Давайте разберем вышеуказанный код.

1. Первая строка убеждается в том, что aspose cells загружен и доступен.
1. Включите файлы, необходимые для доступа к aspose cells.
1. Инициализируйте библиотеки. Классы aspose JAVA загружаются из пути, указанного в файле aspose.yml/
