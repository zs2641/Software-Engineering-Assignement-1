# Software-Engineering-Assignment-1

## UC 1.01

**Name und Identifikationsnummer:** UC 1.01.-Proband:in anlegen  
**Beschreibung:** es werden verschiedene Proband:in angelegt  
**Beteiligte Akteure:** Diagnostiker:in, Proband:in   
**Status:** in Arbeit  
**Auslöser:** Durchführung einer standartisierten Leistungsdiagnostik  
**Vorbedingung:** keine  
**Invariante:** Aufzeichnung der bis zum Abbruch erhobenen Daten  
**Nachbedingung/Ergebnis:** UC 1.01. Proband:innen wurden angelegt  
**Standardablauf:** Alle Daten der Proband:innen werden angelegt und gespeichert  
**Änderungsgeschichte:** 0.01; 15.03.2025.; Sophia Österle  

## UC 1.03
**Name und Identifikationsnummer:** UC 1.03 - Warnung bei Maximalpulsüberschreitung 

**Beschreibung:** Eine Warnung wird angezeigt, wenn der Maximalpuls überschritten wird.

**Beteiligte Akteure:** Diagnostiker:in

**Status:** in Arbeit

**Auslöser:** Überschreiten des Maximalpulses 

**Vorbedingung:** Der Test läuft, und der Puls wird erfasst.

**Invariante:** Die Warnung wird unabhängig von anderen Faktoren ausgelöst, wenn eine Abweichung erkannt wird

**Nachbedingung/Ergebnis:** Der Diagnostiker/die Diagnostikerin wurde über die Abweichung informiert und kann den Test abbrechen

**Standardablauf: Das System überwacht kontinuierlich die Pulswerte.
Sobald eine Abweichung erkannt wird, wird eine Warnung generiert.
Die Warnung wird auf dem Bildschirm des Diagnostikers angezeigt.

**Änderungsgeschichte:** 0.01; 17.03.2025; Sophie Zembacher


## UC 1.06

**Name und Identifikationsnummer:** UC 1.06 Anstrengungsbewertung mittels BORG-Skala durch Proband:in  
**Beschreibung:** Proband:in bewertet die empfundene Anstrengung nach dem Leistungstest mittels BORG-Skala  
**Beteiligte Aktuere:** Proband:in; Diagnostiker:in  
**Status:** in Arbeit  
**Auslöser:** Leistungstest wurde abgeschlossen 
**Vorbedingung:** Proband:in nimmt an Leistungstest teil; BORG-Skala als Angabemöglichkeit verfügbar
**Invariante:** Bewertung erfolgt subjektiv durch Proband:in  
**Standardablauf:** 1. Leistungstest wurde abgeschlossen  
2. System fordert Proband auf Anstrengung mittels Borg Skala zu bewerten  
3. Proband wählt Wert zw. 0(min) und 10(max)  
4. System speichert Angabe
5. Prozess abgeschlossen 

**Änderungsgeschichte:** 0.01; 17.03.2025; Tamira Grubbauer




