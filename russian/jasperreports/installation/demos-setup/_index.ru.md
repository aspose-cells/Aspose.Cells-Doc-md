---
title: Настройка демонстраций
type: docs
weight: 40
url: /ru/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

Aspose.Cells for JasperReports включает ряд демонстрационных проектов, которые помогут вам начать экспортировать отчеты в форматы документов Excel Microsoft из вашего приложения.

Демонстрации, предоставленные с номером Aspose.Cells for JasperReports, являются стандартными демонстрациями JasperReports, модифицированными для демонстрации использования новых экспортеров.

{{% /alert %}}

Чтобы запустить демоверсии Aspose.Cells for JasperReports, выполните следующие действия:

1.  Загрузите JasperReports (например,<https://sourceforge.net/projects/jasperreports/files/archive/>). Обязательно загрузите весь заархивированный проект с исходным кодом и демоверсиями, а не только один JAR.
1. Распакуйте заархивированный проект в какое-нибудь место на жестком диске, например C:\.
1.  Скопируйте все демонстрационные папки из папки \demo**Aspose.Cells.JasperReports.zip** к**\<InstallDir>\demo\samples**, куда "\<InstallDir>" — это место, куда вы распаковали JasperReports. Этот шаг необходим, потому что сценарии демонстрационной сборки основаны на структуре папок JasperReports, в противном случае вам потребуется изменить сценарии сборки.
1.  Копировать**aspose.cells.jasperreports.jar** из папки \lib Aspose.Cells.JasperReports.zip в**\<Каталог_установки>\lib**.
1.  Подготовьте Ant Build Tool и Ivy Dependency Manager, см.**\<Каталог_установки>\readme.txt**.
1.  Изменить**build.xml** в**\<InstallDir>\demo\samples**, добавьте aspose.cells.jasperreports.jar в путь к классам:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1.  Измените текущий каталог на**\<InstallDir>\demo\hsqldb** и запустите следующую командную строку:
   **муравей**
1.  Измените текущий каталог на одну из демонстраций Aspose.Cells for JasperReports, например**\<InstallDir>\demo\samples\ac.charts** и выполните следующие команды в командной строке:
   **муравьиный тест** - для создания файлов отчетов с помощью экспортера XLS Aspose.
1.  Откройте один из полученных документов для просмотра, например**\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** в Microsoft Excel или другом приложении.
