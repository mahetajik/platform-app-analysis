# platform-app-analysis

# 1. Android Package (APK) File Analysis (ClassyShark)
## 1.1 Downloading ClassyShark 
These steps explain how to download [ClassyShark](https://github.com/google/android-classyshark), an inspection tool that opens Android Packages. 
1. Download the [Java Developer Kit](https://www.oracle.com/java/technologies/downloads/#jdk20-mac) for your operating system from [Oracle](https://www.oracle.com/java/technologies/downloads/#jdk20-mac).
2. Download [ClassyShark from GitHub](https://github.com/google/android-classyshark) by running the following: `java -jar ClassyShark.jar` and downloading the asset ClassyShark.jar. 

## 1.2 Opening APKs in ClassyShark 
These steps explain how to open Android Packages using ClassyShark. 
1. Download an APK from [APKPure](https://apkpure.com). Note that there are numerous versions of applications on [APKPure](https://apkpure.com/). For example, [TikTok's APK](https://apkpure.com/tiktok-musically/com.zhiliaoapp.musically/versions) includes versions up until 30.3.4 (as of July 7, 2023). 
2. Drag and drop the APK file onto ClassyShark. There is an option to open files from your folders through ClassyShark but this does not always work. 

## 1.3 Exporting Files from ClassyShark 
These steps explain how to export files opened with ClassyShark. The export button for ClassyShark was flagged as an issue in 2017 in the [Issues section of the ClassyShark GitHub repository](https://github.com/google/android-classyshark/issues/152?fbclid=IwAR0i_hVIFBIpVXwaBGqoXUSjQ-stC1J_R1UJ3S7K2qPoNz0ee1KC0WqQYGE). The creator of the tool developed [alternative tools](https://medium.com/@BorisFarber/exporting-data-from-classyshark-e3cf3fe3fab8) for exporting, but these alternatives seem to have been deprecated. Another user developed a [workaround](https://github.com/google/android-classyshark/issues/152) which works well. Here are the steps to export files out of ClassyShark using that workaround:
1. Ensure that the Android package (APK file) has been downloaded from [AKPure](https://apkpure.com/) and that it's open in ClassyShark. Note the location of the APK file (e.g., downloads, desktop, etc.). Most likely, if the .apk file hasn't been moved, it will be in the "downloads" folder.
2. Open "Mac Terminal" or the "Windows Command Prompt"—command-line interfaces (cli). 
3. Find the APK file using the command-line interface. Change directories by typing "cd" (change directory) and location, e.g., "Downloads."
4. After navigating to the correct directory for the APK file, export any of the files available in ClassyShark. For example, to export the Android Manifest file which contains permissions for [TikTok's Android package](https://apkpure.com/tiktok-musically/com.zhiliaoapp.musically), type the following into the command-line interface: `java -jar ClassyShark.jar -export TikTok_29.7.4_Apkpure.apk AndroidManifest.xml`. Replace AndroidManifest.xml with the name of any file open in ClassyShark. 
5. Locate the file on the computer (likely downloads) as .file extension_dump. In the case of the AndroidManifest.xml file, the name of the exported file will be AndroidManifest.xml_dump. Rename the file. 

## 1.4 Extracting User Permissions from Android Manifest File 
User permissions can be found in the Android Manifest XML file exported from ClassyShark. The file tends to produce an error suggesting an issue with tags. If tags are closed and the file is readable, the Python module [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) can be used. This was not the case for most APK Android Manifest files so a script to parse the files was created. It can be found at: 
platform-app-analysis/classyshark_analysis/permissions_analysis/[permissions_extraction.py](https://github.com/mahetajik/platform-app-analysis/blob/main/classyshark_analysis/permissions_analysis/permissions_extraction.py). 
Permissions are written into a csv file and match the number of permissions listed for the respective app on [APKPure](https://apkpure.com/tiktok-musically/com.zhiliaoapp.musically) (serves as confirmation). 

## 1.5 Extracting List of SDKs from Android Package File 
SDKs are presented in hierarchical pie-like diagrams on ClassyShark. For easier analysis, they can be extracted similar to permissions from the DEX files. 
1. Export all the files contained in ClassyShark for the chosen Android package by typing the following into the command-line interface: `java -jar ClassyShark.jar -export TikTok_29.7.4_Apkpure.apk` (recall 1.3). This will produce files which include all_classes.txt, all_methods.txt, all_strings.txt, and method_counts.txt. 
2. Modify the files by changing their endings to .csv. 
3. Parse the newly created csv files for SDKs using the example Python code found at: platform-app-analysis/classyshark_analysis/sdk_analysis/[sdk_extraction.py](https://github.com/mahetajik/platform-app-analysis/blob/main/classyshark_analysis/sdk_analysis/sdk_extraction.py). 

# 2. Network Analysis (Charles)
[Charles](https://www.charlesproxy.com/) is a web debugging proxy that can be used to monitor internet traffic. For information on how to install and explore social media platform traffic with Charles, see the PDF file at: 
platform-app-analysis/charles_analysis/[instructions_and_exploration.pdf](https://github.com/mahetajik/platform-app-analysis/blob/main/charles_analysis/instructions_and_exploration.pdf). This file also points out the limitations of Charles for analyzing platform data flows. 
