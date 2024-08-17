"use client"

import { Button } from "./button"
import { Card, CardTitle } from "./card"

export default function ClientCard({projects}) {
    return (
        <div>
            <main className="flex min-h-screen flex-col items-center justify-between p-24">
                <h1> Hello from next app</h1>
                {
                    projects?.map((project) => {
                        return (
                            <Card key={project.id}>
                                <CardTitle>{project.title}</CardTitle>
                            </Card>
                        )
                    })
                }
                <Button> Click Me</Button>
            </main>
        </div>
    )
}