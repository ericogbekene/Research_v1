"use client"


export default async function clientCard(projects: type) {
    return (
        <div>
            <main className="flex min-h-screen flex-col items-center justify-between p-24">
                <h1> Hello from next app</h1>
                {projects.map(project => {
                    <Card key={project.id}>
                    </Card>
                })}
                <Button> Click Me</Button>
            </main>
        </div>
    )
}