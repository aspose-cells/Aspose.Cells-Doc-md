---
title: Demo Kurulumu
type: docs
weight: 40
url: /tr/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

JasperReports için Aspose.Cells, uygulamanızdan raporları Microsoft Excel belge biçimlerine aktarmaya başlamanıza yardımcı olacak bir dizi demo proje içerir.

JasperReports için Aspose.Cells ile sağlanan demolar, yeni ihracatçıların kullanımını göstermek için değiştirilmiş standart JasperReports demolarıdır.

{{% /alert %}}

JasperReports demoları için Aspose.Cells'i çalıştırmak üzere aşağıdaki adımları gerçekleştirin:

1.  JasperReports'u indirin (örn.<https://sourceforge.net/projects/jasperreports/files/archive/>). Yalnızca tek bir JAR değil, kaynak kodu ve demolarla birlikte tüm arşivlenmiş projeyi indirdiğinizden emin olun.
1. Arşivlenen projeyi sabit diskinizde bir konuma, örneğin C:\ paketinden çıkarın.
1.  \demo klasöründeki tüm demo klasörlerini kopyalayın.**Aspose.Cells.JasperReports.zip** ile**\<InstallDir>\demo\samples**, nerede "\<InstallDir>", JasperReports'u paketinden çıkardığınız konumdur. Bu adım gereklidir, çünkü demo derleme betikleri JasperReports'un klasör yapısını kullanır, aksi takdirde derleme betiklerini değiştirmeniz gerekir.
1.  Kopyala**aspose.cells.jasperreports.jar** Aspose.Cells.JasperReports.zip dosyasının \lib klasöründen**\<InstallDir>\lib**.
1.  Ant Build Tool ve Ivy Dependency Manager'ı hazırlayın, bkz.**\<InstallDir>\readme.txt**.
1.  Değiştirmek**build.xml** de**\<InstallDir>\demo\samples**, aspose.cells.jasperreports.jar'ı sınıf yoluna ekleyin:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. Geçerli dizini olarak değiştir**\<InstallDir>\demo\hsqldb** ve aşağıdaki komut satırını çalıştırın:
   **karınca çalıştırma Sunucusu**
1.  Geçerli dizini, örneğin JasperReports demoları için Aspose.Cells'den birine değiştirin**\<InstallDir>\demo\samples\ac.charts** ve komut satırında aşağıdaki komutları çalıştırın:
   **karınca testi** - Aspose XLS ihracatçısını kullanarak rapor dosyaları oluşturmak için.
1.  Görüntülemek için ortaya çıkan belgelerden birini açın, örneğin**\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** Microsoft Excel veya başka bir uygulamada.
