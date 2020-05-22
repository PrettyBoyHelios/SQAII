# Business Case for Android Testing Suite
May 20th, 2020  
SDET: *Luis Enrique Correa Morán*

## Table of Contents
1. [Scope](#10-scope)
2. [Approach](#20-approach-architecture)
3. [High Level Architecture & Process](#30-high-level-architecture--process)
4. [Level of Effort](#40-level-of-effort)
5. [Return of Investment](#50-return-of-investment)
6. [Project Benefits](#60-project-benefits)

## 1.0 Scope
The framework to be developed must cover the following requirements.
* Ability to test the correct functionality for the following Android Modules.
    * Phone App
    * Calculator App
    * Android
    
Android versions to be contained in the development process are defined below.
* Android 7 Nougat
* Android 8.0 Oreo
* Android 9.0 Pie
* Android 10.0 Q

Later versions of Android (9.0 & 10.0) will be prioritized as they have just recently entered the mainstream market, and hardly any bugs are likely to be found in earlier versions of the system. Especially given the fact that the Phone and Calculator apps are updated through the Google Play Store making Android fragmentation less of an issue.

Hardly any version of Android is similar to that of another OEM, *Personalization Layers* have been a trend in Android since 2008, and makes it harder to develop a highly optimized and scalable testing framework for all Android Flavors. Only AOSP Android and variants that resemple Pure Android versions will be considered for the framework.

Popular brands that follow this Software trend are described below, important to say that the list is representative and there may be other brands/manufacturers missing.

* Motorola Moto Series
* Google Pixels Series
* Motorola One Series
* Google Nexus Series
* OnePlus Series
* Nokia devices after 2016
* Xiaomi MI A3
* Redmi Go
* Some models of ASUS Zenphone
* PocoPhone Series

### 1.1 Reliability Test
The test aims to achieve reliability by reproducing consistent test cases (independent of Android version) among multiple devices. As well as having assertions on conditions that prove that the ultimate goal of a given test case is fulfilled.

### 1.2 Framework Mechanism
* SDK: E2E UI Workflow, that carries out human-like procedures on apps by simulating human interaction.
* GUI: Script Oriented and CLI tools available for the framework utilization.
* Log & Autoreporting: the framework will be able of generating the same logs a manual tester would and generate a csv report of them.
* History Reporting System: an historical archive of test runs will be created.
* Test Scheduler: the frameork is meant to be run at least once every day, though if multiple builds are generated in a day, it is possible to run them multiple times.
* Scalability for Devices: the framework won't run on simultaneous devices, but is able to add multiple devices on a run, so that tests on a device are executed right after the previous device finishes.
* Flexibility: Adiition of new test cases ir really easy, as well as new test assertions. Suites usually require a time consuming supporting library to be created, but test Suite addition is usually easy and fast.

## 2.0 Approach Architecture
The platform will be built on top of the Android Platform, over which the language python will be the base for developing any script or supporting library the framework requires.
Auxiliary formats like JSON and CSV will be used so that the framework is able of interacting with human readable elements for test input and output.

OpenSource libraries such as UIAutomator, ADB Shell and Python Open Source libraries will be used to create Supporting Libraries that will contain useful and repetitive tasks used by Testing Suites, that perform testing over an Android Module or App.
![Architecture](img/architecture.png)

## 3.0 High Level Architecture & Process
![High LevelArquitecture](img/architecture_2.png)

## 4.0 Level of Effort
|                          | F        | S        | S        | M        | T        | W        | T        | F        | S        |           |    |
|--------------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|----|
| Task Activity            | 15/05/20 | 16/05/20 | 17/05/20 | 18/05/20 | 19/05/20 | 20/05/20 | 21/05/20 | 22/05/20 | 23/05/20 | Time/Task |    |
| Total Hours              | 3        | 6        | 5        | 3        | 3        | 4        | 3        |          |          | 27        |    |
| Tool Analysis            | 3        | 1        |          |          |          |          |          | Demo     | Demo     | 4         | 17 |
| Test Case Design         |          | 2        |          |          |          |          |          |          |          | 2         |    |
| Library Development      |          | 3        | 1        |          |          |          |          |          |          | 4         |    |
| PhoneCall Refactor       |          |          | 2        |          |          |          |          |          |          | 2         |    |
| Test Case Implementation |          |          | 2        | 1        |          |          |          |          |          | 3         |    |
| Test Execution & Fixes   |          |          |          | 2        |          |          |          |          |          | 2         |    |
| Test Plan                |          |          |          |          | 3        |          |          |          |          | 3         |    |
| Business Plan            |          |          |          |          |          | 2        |          |          |          | 2         |    |
| Repo Final Update        |          |          |          |          |          | 2        | 1        |          |          | 3         |    |
| Demo Rehearsal           |          |          |          |          |          |          | 2        |          |          | 2         |    |

## 5.0 Return of Investment

## 6.0 Project Benefits
