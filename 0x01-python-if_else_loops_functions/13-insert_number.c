#include <stdio.h>
#include <stdlib.h>

/* Definition of a singly linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to insert a number into a sorted singly linked list */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL; // Return NULL if memory allocation fails
    }
    new_node->n = number;
    new_node->next = NULL;

    listint_t *current = *head;
    listint_t *prev = NULL;

    while (current != NULL && current->n < number) {
        prev = current;
        current = current->next;
    }

    if (prev == NULL) {
        new_node->next = *head;
        *head = new_node;
    } else {
        prev->next = new_node;
        new_node->next = current;
    }

    return new_node; // Return the address of the new node
}
