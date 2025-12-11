---
title: Using Aspise.Cells for Java with Perl
type: docs
weight: 30
url: /java/using-aspose-cells-for-java-with-perl/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells for Java is a pure Java component that can be used with Perl. Using the component is the same as invoking other common Java APIs in Perl. To call any Java library in Perl, you need to install the Java‑Perl extension for Perl first. This is needed to access the JVM.

{{% /alert %}} 

## **Required Software and Libraries**
The following software and libraries are required. 

- Perl.
- Aspose.Cells for Java.
- Java‑Perl extension.
- Java runtime that meets the requirements of Aspose.Cells for Java and the Java‑Perl extension.

### **Guide**
To call a Java API in Perl, you need to install the Java‑Perl extension for Perl first. (For the purposes of this article, we assume that Perl has been installed and set properly.) You can get the Java‑Perl extension from [METZZO/Java-4.7](https://metacpan.org/release/METZZO/Java-4.7).

At the end of this document, there is an example of a Perl script that calls Aspose.Cells for Java. To run it, follow the steps below: 

1. Download the file `Java-4.7.tar.gz` and unzip it to your local drive.  
2. Install this package for Perl.  
3. Start JavaServer. The command will be: 

{{< highlight java >}}
java -classpath ...  com.zzo.javaserver.JavaServer 
{{< /highlight >}}

where `...` is the classpath that must include all the libraries required by your application. 

To use Aspose.Cells for Java, you should have at least two JAR files:

1. **Aspose.Cells.jar** from Aspose.Cells for Java  
2. **JavaServer.jar** from `Java-4.7.tar.gz`  

3. Run the Perl script which invokes the Aspose.Cells for Java API.

For more information on how to work with Java in Perl, see the documentation of the Java‑Perl extension at <https://metacpan.org/release/METZZO/Java-4.7>.

**Perl**

{{< highlight perl >}}
my $ok = 0;

BEGIN { $| = 1; print "1..33\n"; }

END {print "not ok $ok - is JavaServer on localhost running?\nJavaServer must be running for these tests to function.\n" unless $loaded;}

BEGIN {
    print "WARNING: You cannot run these tests unless JavaServer is running!\n";
    print "Do you want to continue? (Y/n) ";
    my $in = <STDIN>;
    exit 1 if ($in =~ /^n/i);
}

use lib '.';
use Java;

my $java = new Java();
$loaded = 1;
$ok++;

print "ok $ok\n";

my $workbook = $java->create_object("com.aspose.cells.Workbook");
$ok++;
print "workbook $ok\n";

#$workbook->open("t.xls");
$ok++;
print "open $ok\n";

my $worksheets = $workbook->getWorksheets();
$ok++;
print "worksheets $ok\n";

my $worksheet = $worksheets->get(0);
$ok++;
print "worksheet $ok\n";

my $cells = $worksheet->getCells();
$ok++;
print "cells $ok\n";

my $cell = $cells->getCell(0,1);
$ok++;
print "cell $ok\n";

$cell->setValue(123);
$cell = $cells->getCell(1,1);
$cell->setValue(456);
$cell = $cells->getCell(2,1);
$cell->setFormula("=SUM(B1:B2)");
$cell = $cells->getCell(3,1);
$cell->setValue("abc");
$workbook->save("t1.xls");
$ok++;
print "save $ok\n";
{{< /highlight >}}
