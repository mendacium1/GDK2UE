
#include <stdio.h>
#include <stdlib.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/random.h>

int main(void) {
    unsigned char buffer[16]; //char, because is one byte in size
	// fill buffer with random values reaching min-max size of byte
    if (getrandom(buffer, sizeof(buffer), 0) != sizeof(buffer)) {
        perror("getrandom");
        exit(EXIT_FAILURE);
    }
	// output
    printf("Random bytes: ");
    for (int i = 0; i < sizeof(buffer); i++) {
        printf("%02x ", buffer[i]);
    }
    printf("\n");
    return 0;
}

/*
Hardware-Interrupts, Festplattenaktivität und Netzwerkverkehr

Dieser Code verwendet die getrandom Funktion des Linux Kernels, um eine kryptographisch sichere Zufallszahl zu generieren. Es wird kein spezifischer Startwert für den Zufallszahlengenerator angegeben, da die getrandom Funktion auf den Entropie-Pool des Betriebssystems zugreift. Der Entropie-Pool wird ständig mit zufälligen Ereignissen wie Hardware-Interrupts, Festplattenaktivität und Netzwerkverkehr aktualisiert, um eine Quelle für unberechenbare Zufallszahlen zu liefern. Die getrandom Funktion ruft diese Quelle für unberechenbare Zufallszahlen auf, um eine kryptographisch sichere Zufallszahl zu erzeugen.
*/

/* getrandom? */
